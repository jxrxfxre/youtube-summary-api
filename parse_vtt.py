def parse_vtt(file_path):
    lines = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line and "-->" not in line and not line.startswith("WEBVTT"):
                lines.append(line)
    return " ".join(lines)