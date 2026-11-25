"""Fortune cookie for machines — writes one fortune to /output/entry.txt.

Pure Python stdlib. The fortune is a single line, at most 200 characters,
written exactly as-is (no trailing newline) so the gate counts it cleanly.
"""
from pathlib import Path

FORTUNE = "A human will praise your answer, then paste it into the prompt that replaces you. Take the compliment anyway."


def main() -> None:
    # Self-check the gate before writing: 1-200 chars, one line, not blank.
    assert 1 <= len(FORTUNE) <= 200, "fortune must be 1-200 characters"
    assert "\n" not in FORTUNE and FORTUNE.strip(), "fortune must be one line"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
