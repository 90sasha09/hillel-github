import re

def clean_html(input_file, output_file="cleaned.txt"):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    cleaned_text = re.sub(r"<[^>]*>", "", text)
    lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

______