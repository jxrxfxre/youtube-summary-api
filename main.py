
from subtitle_extractor import download_subtitle
from parse_vtt import parse_vtt
from summarize import summarize_text
from api_main import app

def main():
    url = input("유튜브 링크를 입력하세요: ").strip()
    download_subtitle(url)

    text = parse_vtt("subtitle.ko.ko.vtt")
    print("\n추출된 자막 일부분:")
    print(text[:500])

    summary = summarize_text(text)
    print("\nGPT 요약 결과:")
    print(summary)

if __name__ == "__main__":
    main()