from PIL import Image
from pathlib import Path
import os


def resize_image(input_path, output_path, n):
    image = Image.open(input_path)

    new_width = image.width // n
    new_height = image.height // n

    resized = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    resized.save(output_path)


def main(path: Path, n: int):
    to_path = path.joinpath(f"x{n}")
    if not to_path.exists():
        to_path.mkdir()

    for file in path.joinpath("x1").iterdir():
        resize_image(str(file.absolute()), str(to_path.joinpath(file.name).absolute()), n)


if __name__ == "__main__":
    main(Path("assets"), 2)
