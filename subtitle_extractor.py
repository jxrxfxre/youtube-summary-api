
from yt_dlp import YoutubeDL
import requests

def download_subtitle(url: str) -> str:
    ydl_opts = {
        "skip_download": True,
        "writesubtitles": True,
        "subtitleslangs": ["ko", "ko-KR"],
        "subtitlesformat": "vtt",
        "quiet": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        if "subtitles" in info and "ko" in info["subtitles"]:
            sub_url = info["subtitles"]["ko"][0]["url"]
            return requests.get(sub_url).text
        return ""
