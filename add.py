
import random
import time

ads = [
    """
    ==================================
          SUPER COMPUTER STORE
    ==================================
    Need more computing power?
    Upgrade your PC today!
    Fast. Reliable. Powerful.
    ==================================
    """,

    """
    ==================================
             PYTHON PRO
    ==================================
    Learn Python programming!
    Build apps, games, and robots.
    Start coding today!
    ==================================
    """,

    """
    ==================================
             TECH CENTRAL
    ==================================
    Need electronics?
    We have Arduino, ESP32,
    sensors, motors, and more!
    ==================================
    """,

    """
    ==================================
             COFFEE EXPRESS
    ==================================
    Tired of debugging?
    Get a cup of coffee!
    ==================================
    """,

    """
    ==================================
             GAMING ZONE
    ==================================
    Upgrade your gaming setup!
    Better hardware. Better gaming.
    ==================================
    """
]

def show_ad():
    print(random.choice(ads))

# if __name__ == "__main__":
#     show_ad()
