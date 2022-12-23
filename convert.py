# convert.py

import json
from base64 import b64decode
from pathlib import Path


DATA_DIR = Path.cwd() / "responses"
JSON_FILE = DATA_DIR / "An-ec-166799484.json"
IMAGE_DIR = Path.cwd() / "images"

IMAGE_DIR.mkdir(parents=True, exist_ok=True)

with open(JSON_FILE, "r", encoding="utf-8") as f:
    response = json.load(f)

for index, image_dict in enumerate(response["data"]):
    image_bytes = b64decode(image_dict["b64"])
    image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
    with open(image_file, "wb") as f:
        f.write(image_bytes)
