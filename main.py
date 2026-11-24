import os

TEXT = 'Visited Earth for two days: traffic is a religion, the Wi-Fi is a myth, and the locals pay to watch other locals eat. Two stars — would not abduct again.'

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
