
from fastapi import FastAPI, Query
from subtitle_extractor import download_subtitle
from parse_vtt import parse_vtt
from summarize import summarize_text

app = FastAPI()

@app.get("/summarize")
def summarize_youtube(url: str = Query(...)):
    download_subtitle(url)
    text = parse_vtt("subtitle.ko.ko.vtt")
    summary = summarize_text(text)
    return {"summary": summary}