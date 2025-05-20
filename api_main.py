
from fastapi import FastAPI, Query
from subtitle_extractor import download_subtitle
from summarize import summarize_text
from parse_vtt import parse_vtt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #실제 서비스 배포시에 프론트 도메인으로 제한하기
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/summarize")
def summarize_youtube(url: str = Query(...)):
    vtt_content = download_subtitle(url)
    if not vtt_content:
        return {"summary": "자막 없는 영상임"}
    
    text = parse_vtt(vtt_content)
    summary = summarize_text(text)
    return {"summary": summary}

@app.get("/")
def root():
    return {"message": "FastAPI 배포 성공"}