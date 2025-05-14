import subprocess

def download_subtitle(url):
    subprocess.run([
        "yt-dlp",
        "--write-auto-sub",
        "--sub-lang", "ko",
        "--skip-download",
        "-o", "subtitle.ko.%(ext)s",
        url
    ])
    print("자막 다운로드 완료!")