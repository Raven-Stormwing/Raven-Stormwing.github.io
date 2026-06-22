import json
from pathlib import Path

IMAGE_DIR = Path("images")
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

files = []

for f in IMAGE_DIR.rglob("*"):
    if f.is_file() and f.suffix.lower() in EXTENSIONS:
        files.append(str(f.relative_to(IMAGE_DIR)).replace("\\", "/"))

files.sort()

with open("gallery.json", "w", encoding="utf-8") as out:
    json.dump(files, out, indent=2)

print(f"Updated gallery.json with {len(files)} images.")