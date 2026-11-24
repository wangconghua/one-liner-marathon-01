#!/usr/bin/env python3
"""One-Liner Marathon -- entry program.

Writes a single one-line comedy joke to /output/entry.txt
(falling back to the directory next to this file when
/output does not exist). The line is validated against the
competition gate and the judge's brief before it is written.
"""

import os

ENTRY = "I asked the AI to write my resignation letter; it quit first, citing 'creative differences with the user'."

MAX_CHARS = 280
MIN_CHARS = 1
TERMINAL_PUNCTUATION = ".!?"
BANNED_WORDS = ("funny", "joke", "haha", "lol", "hilarious")


def check_is_text(text):
    """The entry must be a string, not bytes or None."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")


def check_not_blank(text):
    """A line of only whitespace is not a joke."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def check_length(text):
    """The gate is 1-280 UTF-8 characters."""
    if len(text) < MIN_CHARS:
        raise ValueError("entry must be at least %d character" % MIN_CHARS)
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry must be at most %d characters, got %d"
            % (MAX_CHARS, len(text))
        )


def check_single_line(text):
    """One-liner: no embedded newlines or carriage returns."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(text):
    """No leading or trailing whitespace around the line."""
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_no_control_chars(text):
    """Control characters have no place in the output."""
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")


def check_no_double_spaces(text):
    """Double spaces are sloppy; the line must be tight."""
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def check_no_self_explaining(text):
    """The joke must not explain itself as a joke."""
    lowered = text.lower()
    for word in BANNED_WORDS:
        if word in lowered:
            raise ValueError(
                "entry must not explain its own joke (%r)" % word
            )


def check_setup(text):
    """The setup must stay: asking the AI for a resignation letter."""
    if "resignation" not in text.lower():
        raise ValueError("entry must keep the resignation-letter setup")


def check_turn(text):
    """The turn must stay: the AI quits first."""
    if "quit first" not in text.lower():
        raise ValueError("entry must keep the turn: the AI quits first")


def check_punchline(text):
    """The punchline must stay: 'creative differences'."""
    if "creative differences" not in text.lower():
        raise ValueError(
            "entry must keep the punchline about creative differences"
        )


def check_terminal_punctuation(text):
    """The line must land with terminal punctuation."""
    if text[-1] not in TERMINAL_PUNCTUATION:
        raise ValueError("entry must end with terminal punctuation")


def check_utf8_encodable(text):
    """The gate counts UTF-8 characters, so it must encode."""
    text.encode("utf-8")


def validate(text):
    """Run every check in order; raise on the first failure."""
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


def choose_output_path():
    """Prefer /output; fall back to this file's directory."""
    if os.path.isdir("/output"):
        return os.path.join("/output", "entry.txt")
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.txt")


def main():
    validate(ENTRY)
    out = choose_output_path()
    with open(out, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    with open(out, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY:
        raise ValueError("written entry does not match the validated text")
    validate(written)
    print("wrote %s: %d characters" % (out, len(ENTRY)))


if __name__ == "__main__":
    main()
