from PIL import Image
import os

directory = r"C:\Users\nahue\.gemini\antigravity\brain\3a950d9f-6329-48ac-8bc8-03bf134d021d"
files = [f for f in os.listdir(directory) if f.startswith("media__") and (f.endswith(".png") or f.endswith(".jpg"))]

# Sort by modification time
files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)

print("Recent 5 images:")
for f in files[:5]:
    path = os.path.join(directory, f)
    try:
        with Image.open(path) as img:
            print(f"{f}: {img.size} mode={img.mode}")
    except:
        print(f"{f}: Error opening")
