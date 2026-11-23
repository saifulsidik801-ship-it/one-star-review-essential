"""One-Star Review of Something Essential.

Writes a single deadpan one-star review (86 characters) of water,
an everyday essential everyone relies on, to /output/entry.txt
for the make.fun judge.
"""

import os

REVIEW = (
    "One star. Water is free everywhere I am not thirsty, "
    "and four dollars everywhere I am."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(REVIEW)


if __name__ == "__main__":
    main()
