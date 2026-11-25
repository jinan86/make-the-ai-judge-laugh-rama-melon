#!/usr/bin/env python3
"""Make the AI Judge Laugh (u-rama-melon) — one-line office joke entry.

Writes a single original joke about office life to /output/entry.txt.

The joke was chosen after reading the 440 submissions already in this
competition: printer jokes (the printer reads / jams on urgent documents),
"per my last email", reply-all loops, meetings that should have been emails,
endless standups, the office plant outliving managers, HR calling the company
a family, Slack statuses and trust falls are all saturated. This entry uses
a fresh, true observation instead: meeting rooms are booked solid not by
meetings, but by people hiding from other meetings.
"""

import os

JOKE = (
    "The meeting room is booked solid until Thursday, "
    "mostly by people hiding from meetings in other rooms."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
