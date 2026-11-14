import os
import sys


def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(src, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    if not text or not text.strip():
        raise SystemExit("entry.txt is empty or whitespace-only")
    if len(text) > 1000:
        raise SystemExit("entry.txt exceeds 1000 characters: %d" % len(text))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(data)
    with open(out_path, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("output does not match entry.txt byte for byte")
    print("wrote %s (%d characters, byte-identical)" % (out_path, len(text)))


if __name__ == "__main__":
    main()
