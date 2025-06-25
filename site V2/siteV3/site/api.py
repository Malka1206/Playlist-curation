from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou ["http://localhost:4321"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_audio(audio: UploadFile = File(...)):
    contents = await audio.read()
    tmp_path = "tmp_audio_file"
    with open(tmp_path, "wb") as f:
        f.write(contents)
    result = subprocess.check_output(['python', 'func.py', tmp_path], text=True)
    os.remove(tmp_path)
    return {"result": result.strip()}