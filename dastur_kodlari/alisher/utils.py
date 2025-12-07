import json
import os

def ensure_json(path, default_data):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default_data, f, indent=4)

def load(path):
    with open(path, "r") as f:
        return json.load(f)

def save(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def color(text, c):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "end": "\033[0m"
    }
    return colors[c] + text + colors["end"]
