import sys
def print_intro():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    letters = {
        "A": (" ███ ", "█   █", "█████", "█   █", "█   █"),
        "B": ("████ ", "█   █", "████ ", "█   █", "████ "),
        "D": ("████ ", "█   █", "█   █", "█   █", "████ "),
        "E": ("█████", "█    ", "████ ", "█    ", "█████"),
        "I": ("█████", "  █  ", "  █  ", "  █  ", "█████"),
        "L": ("█    ", "█    ", "█    ", "█    ", "█████"),
        "M": ("█   █", "██ ██", "█ █ █", "█   █", "█   █"),
        "W": ("█   █", "█   █", "█ █ █", "██ ██", "█   █"),
        "Y": ("█   █", " █ █ ", "  █  ", "  █  ", "  █  "),
    }
    message = "MADE BY WILLIAM"
    banner_style = "\033[1;31;42m"
    credit_style = "\033[1;31m"
    reset = "\033[0m"

    rows = []
    for row in range(5):
        pieces = []
        for character in message:
            if character == " ":
                pieces.append("   ")
            else:
                pieces.append(letters[character][row])
        rows.append("       " + " ".join(pieces))

    print()
    for row in rows:
        print(f"{banner_style}{row}  {reset}")
    print(f"{credit_style}       This banner was made with AI{reset}")
    print()


# print_intro()