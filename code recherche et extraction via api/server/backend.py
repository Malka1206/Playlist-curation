from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search_music(q: str = Query(...)):
    url = f"https://api.deezer.com/search?q={q}"
    response = requests.get(url)
    data = response.json()

    if data["data"]:
        preview_url = data["data"][0]["preview"]
        title = data["data"][0]["title"]
        artist = data["data"][0]["artist"]["name"]
        return {
            "preview_url": preview_url,
            "title": title,
            "artist": artist
        }
    else:
        return {"preview_url": None, "title": None, "artist": None}
