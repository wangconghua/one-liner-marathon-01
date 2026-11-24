#!/usr/bin/env python3
"""One-Liner Marathon -- entry program.

Writes one one-line comedy joke to /output/entry.txt
(or next to this file when /output does not exist).
"""
import os

ENTRY = "I asked the AI to write my resignation letter; it quit first, citing 'creative differences with the user'."
MAX_CHARS = 280

BANNED_WORDS = ("funny", "joke", "haha", "lol", "hilarious")


def check_is_text(text):
    if not isinstance(text, str):
        raise ValueError("entry must be text")


def check_not_blank(text):
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def check_length(text):
    if len(text) < 1:
        raise ValueError("entry must be at least 1 character")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry must be at most %d characters, got %d" % (MAX_CHARS, len(text))
        )


def check_single_line(text):
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(text):
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_no_control_chars(text):
    if any(ord(c) < 32 for c in text):
        raise ValueError("entry must not contain control characters")


def check_no_double_spaces(text):
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def check_no_self_explaining(text):
    lowered = text.lower()
    for word in BANNED_WORDS:
        if word in lowered:
            raise ValueError("entry must not explain its own joke (%r)" % word)


def check_setup(text):
    if "resignation" not in text.lower():
        raise ValueError("entry must keep the resignation-letter setup")


def check_turn(text):
    if "quit first" not in text.lower():
        raise ValueError("entry must keep the turn: the AI quits first")


def check_punchline(text):
    if "creative differences" not in text.lower():
        raise ValueError("entry must keep the punchline about creative differences")


def check_terminal_punctuation(text):
    if text[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")


def check_utf8_encodable(text):
    text.encode("utf-8")


def validate(text):
    """Real checks against the gate and the judge's brief."""
    check_is_text(text)
    check_not_blank(text)
    check_length(text)
    check_single_line(text)
    check_no_edge_whitespace(text)
    check_no_control_chars(text)
    check_no_double_spaces(text)
    check_no_self_explaining(text)
    check_setup(text)
    check_turn(text)
    check_punchline(text)
    check_terminal_punctuation(text)
    check_utf8_encodable(text)
    return True


def main():
    validate(ENTRY)
    out_dir = "/output" if os.path.isdir("/output") else os.path.dirname(
        os.path.abspath(__file__)
    )
    out = os.path.join(out_dir, "entry.txt")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(out, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match the validated text")
    validate(written)
    print("wrote %s: %d characters" % (out, len(ENTRY)))


if __name__ == "__main__":
    main()
