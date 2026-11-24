import os


ENTRY = "Visited Earth. The locals are friendly but obsessed with small glowing rectangles, and the food is great if you enjoy waiting in line for it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
