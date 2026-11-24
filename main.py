import os

TEXT = 'Earth review: the food is great, the gravity is rude, and the locals argue with rectangles for eight hours a day. Three stars — would orbit again.'

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
