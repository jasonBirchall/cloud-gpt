# create.py

import json
import os
import sys
from pathlib import Path

import openai

PROMPT = "An eco-friendly computer from the 90s in the syete of vaporware"
DATA_DIR = Path.cwd() / "responses"

DATA_DIR.mkdir(exist_ok=True)

openai.api_key = os.getenv("OPENAI_API_KEY")
if "OPENAI_API_KEY" not in os.environ:
    print("Please set OPENAI_API_KEY.")
    sys.exit(1)

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json",
)

file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"

with open(file_name, "w", encoding="utf-8") as f:
    json.dump(response, f)
