
import hashlib
import secrets
import string
import json
import os

DATABASE = "users.dat"


def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_bytes(16)

    hashed = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        600000
    )

    return salt, hashed


def load_users():
    if not os.path.exists(DATABASE):
        return {}

    with open(DATABASE, "r") as file:
        return json.load(file)


def save_users(users):
    with open(DATABASE, "w") as file:
        json.dump(users, file)


def add_user(username, password):
    users = load_users()

    salt, hashed = hash_password(password)

    users[username] = {
        "salt": salt.hex(),
        "hash": hashed.hex()
    }

    save_users(users)


def login(username, password):
    users = load_users()

    if username not in users:
        return False

    salt = bytes.fromhex(users[username]["salt"])
    stored_hash = bytes.fromhex(users[username]["hash"])

    _, entered_hash = hash_password(password, salt)

    return secrets.compare_digest(
        stored_hash,
        entered_hash
    )


def generate_password(length=32):
    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()-_=+"
    )

    return ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )


