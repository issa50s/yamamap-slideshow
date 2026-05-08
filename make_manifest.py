import os
import json

folders = ["100", "200", "300"]
image_exts = [".png", ".jpg", ".jpeg", ".webp"]

for folder in folders:
    files = [
        f for f in os.listdir(folder)
        if os.path.splitext(f)[1].lower() in image_exts
    ]

    files.sort()

    with open(os.path.join(folder, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(files, f, ensure_ascii=False, indent=2)

    print(folder, len(files), "files")