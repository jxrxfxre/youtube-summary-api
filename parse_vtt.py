
def parse_vtt(vtt_content: str) -> str:
    lines = vtt_content.splitlines()
    results = []
    for line in lines:
        if "-->" in line or line.strip() == "":
            continue
        results.append(line.strip())
    return " ".join(results)