from __future__ import annotations
from collections import Counter
from pathlib import Path
from typing import List


def tokenize(text: str) -> List[str]:
    text = text.lower()
    cleaned_chars = []
    for ch in text:
        if ch.isalnum() or ch in ("'", "’"):
            cleaned_chars.append(ch)
        else:
            cleaned_chars.append(" ")
    cleaned = "".join(cleaned_chars)

    tokens = [t for t in cleaned.split() if t]
    return tokens


def analyze_text_file(input_path: Path, output_path: Path) -> None:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with input_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)

    words: List[str] = []
    for line in lines:
        words.extend(tokenize(line))

    total_words = len(words)
    freq = Counter(words)

    sorted_items = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

    with output_path.open("w", encoding="utf-8") as out:
        out.write(f"Total lines: {total_lines}\n")
        out.write(f"Total words: {total_words}\n")
        out.write("\nWord frequency:\n")
        for word, count in sorted_items:
            out.write(f"{word}: {count}\n")


def main() -> None:
    here = Path(__file__).resolve().parent
    input_path = here / "text.txt"
    output_path = here / "analysis.txt"

    analyze_text_file(input_path, output_path)
    print(f"Done. Results saved to: {output_path}")


if __name__ == "__main__":
    main()
