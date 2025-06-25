from fastapi import FastAPI, UploadFile, File, Body
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import uuid
import requests
import tempfile
import func
import func2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-v2")
async def analyze_v2(audios: list[UploadFile] = File(...)):
    # Crée un dossier temporaire unique
    tmp_dir = f"tmp_{uuid.uuid4().hex}"
    os.makedirs(tmp_dir, exist_ok=True)
    file_paths = []
    try:
        for audio in audios:
            file_path = os.path.join(tmp_dir, audio.filename)
            with open(file_path, "wb") as f:
                shutil.copyfileobj(audio.file, f)
            file_paths.append(file_path)
        # Appelle func2.analyze_musics
        result = func2.analyze_musics(file_paths)
        return result
    finally:
        # Nettoie le dossier temporaire
        for fp in file_paths:
            if os.path.exists(fp):
                os.remove(fp)
        try:
            if os.path.exists(tmp_dir):
                shutil.rmtree(tmp_dir)
        except Exception as e:
            print(f"Erreur lors de la suppression du dossier temporaire: {e}")

@app.post("/analyze-preview")
def analyze_preview(url: str = Body(...)):
    # Télécharge le mp3 dans un fichier temporaire
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        r = requests.get(url, stream=True)
        for chunk in r.iter_content(chunk_size=8192):
            tmp.write(chunk)
        tmp_path = tmp.name
    try:
        # Appelle ta fonction d'analyse sur le fichier temporaire
        genre = func.analyze_audio(tmp_path)
        return {"genre": genre}
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)