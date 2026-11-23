import subprocess
import sys
from pathlib import Path


def main():
    while True:
        mode = input("Choose game mode: terminal or web: ").strip().lower()
        if mode in ("terminal", "t"):
            subprocess.run([sys.executable, str(Path(__file__).with_name("run.py"))], check=False)
            return
        if mode in ("web", "w"):
            import webmode

            webmode.start_server()
            return
        print("Please enter terminal or web.")


if __name__ == "__main__":
    main()
