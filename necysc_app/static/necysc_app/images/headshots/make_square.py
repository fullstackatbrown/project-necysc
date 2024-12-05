from PIL import Image
import os

def crop_to_square(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        min_dimension = min(width, height)
        left = (width - min_dimension) / 2
        top = (height - min_dimension) / 2
        right = (width + min_dimension) / 2
        bottom = (height + min_dimension) / 2

        img_cropped = img.crop((left, top, right, bottom))
        img_cropped.save(image_path)

def crop_all_images_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            image_path = os.path.join(directory, filename)
            crop_to_square(image_path)
            print(f'Cropped {filename}')

if __name__ == "__main__":
    current_directory = os.getcwd()
    crop_all_images_in_directory(current_directory)