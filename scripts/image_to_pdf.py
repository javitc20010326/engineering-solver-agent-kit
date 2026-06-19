from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert one or more images into a PDF.")
    parser.add_argument("output", help="Output PDF")
    parser.add_argument("images", nargs="+", help="Input images")
    args = parser.parse_args()

    try:
        from PIL import Image
    except ImportError as exc:
        raise SystemExit("Pillow is required: pip install pillow") from exc

    output = Path(args.output)
    pil_images = []
    for image in args.images:
        pil_images.append(Image.open(image).convert("RGB"))

    output.parent.mkdir(parents=True, exist_ok=True)
    first, rest = pil_images[0], pil_images[1:]
    first.save(output, save_all=True, append_images=rest, resolution=150)
    for image in pil_images:
        image.close()
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
