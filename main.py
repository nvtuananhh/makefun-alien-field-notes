import os

# Alien Field Notes: an alien tourist's one-line review of Earth.
# The laugh comes from the visitor's angle on ordinary Earth life:
# locals pay to be shouted at while running in place, then pay to
# sit in hot water — and the best thing on the planet is free.
ENTRY = "The locals pay $40 an hour to be shouted at while running in place, then $30 to sit in hot water. Four stars; the sunsets are free."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
