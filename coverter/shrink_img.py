import os
from PIL import Image


def shrink_image(input_path, output_path, shrink_percentage):
    try:
        with Image.open(input_path) as img:
            width, height = img.size
            print(f"Original size: {width}x{height}")

            new_width = int(width * shrink_percentage / 100)
            new_height = int(height * shrink_percentage / 100)

            img = img.resize((new_width, new_height), Image.LANCZOS)

            # Preserve image orientation
            if width < height:
                print(f"Rotating {input_path}...")
                img = img.rotate(270, expand=True)

            img.save(output_path)
    except Exception as e:
        print(f"An error occurred while processing {input_path}: {e}")


def shrink_images_in_directory(directory, shrink_percentage):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory,
                                       f"_shrunken{os.path.splitext(filename)[0]}{os.path.splitext(filename)[1]}")
            shrink_image(input_path, output_path, shrink_percentage)
            print(f"Resized: {input_path} => {output_path}")


if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    shrink_percentage = 80  # Adjust the percentage as needed

    shrink_images_in_directory(current_directory, shrink_percentage)
