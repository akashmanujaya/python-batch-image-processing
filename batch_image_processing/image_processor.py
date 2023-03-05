import os
from typing import List

from PIL import Image, ImageFilter, UnidentifiedImageError


def _make_directory(path) -> None:
    folder_path = os.path.dirname(path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


class ImageProcessor:
    def __init__(self, image_folder: str, process_folder: str):
        self.image_folder = image_folder
        self.process_folder = process_folder
        self.valid_formats = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff")

    def _get_image_paths(self, folder: str) -> List[str]:
        """
        Returns a list of file paths to all image files in the given folder and its subfolders.
        """
        try:
            file_names = os.listdir(folder)
        except FileNotFoundError:
            raise Exception("Image folder does not exist.")

        image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff"]
        image_paths = []

        for file_name in file_names:
            file_path = os.path.join(folder, file_name)
            try:
                if (
                    os.path.isfile(file_path)
                    and os.path.splitext(file_name)[1].lower() in image_extensions
                ):
                    image_paths.append(file_path)
                elif os.path.isdir(file_path):
                    # Recursively call this function on subdirectories
                    subfolder_paths = self._get_image_paths(file_path)
                    if subfolder_paths:
                        image_paths.extend(subfolder_paths)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

        return image_paths

    def _get_all_image_paths(self) -> List[str]:
        """
        Returns a list of file paths to all image files in the image folder and its subfolders.
        """
        return self._get_image_paths(self.image_folder)

    def resize_images(self, width: int, height: int) -> None:
        """
        Resizes all images in the image folder and its subfolders to the specified width and height
        and saves them to the process folder.
        """
        image_paths = self._get_all_image_paths()
        for path in image_paths:
            try:
                with Image.open(path) as image:
                    resized_image = image.resize((width, height))
                    new_path = os.path.join(
                        self.process_folder, os.path.relpath(path, self.image_folder)
                    )

                    # making the directory inside the destination if not exits
                    _make_directory(new_path)

                    resized_image.save(new_path)
            except (
                FileNotFoundError,
                UnidentifiedImageError,
                OSError,
                Exception,
            ) as error:
                print(f"An error occurred while processing {path}: {error}")

    def crop_images(self, left: int, top: int, right: int, bottom: int) -> None:
        """
        Crops all images in the image folder using the specified coordinates
        and saves them to the process folder.
        """
        image_paths = self._get_all_image_paths()
        for path in image_paths:
            try:
                with Image.open(path) as image:
                    cropped_image = image.crop((left, top, right, bottom))
                    new_path = os.path.join(
                        self.process_folder, os.path.relpath(path, self.image_folder)
                    )

                    # making the directory inside the destination if not exits
                    _make_directory(new_path)

                    cropped_image.save(new_path)
            except (
                FileNotFoundError,
                UnidentifiedImageError,
                OSError,
                Exception,
            ) as error:
                print(f"An error occurred while processing {path}: {error}")

    def convert_images(self, image_format: str) -> None:
        """
        Converts all images in the image folder to the specified format
        and saves them to the process folder.
        """
        image_paths = self._get_all_image_paths()
        for path in image_paths:
            try:
                with Image.open(path) as image:
                    new_format = image_format.lower()
                    if new_format == "jpg":
                        new_format = "jpeg"
                    new_path = os.path.join(
                        self.process_folder,
                        os.path.splitext(os.path.relpath(path, self.image_folder))[0]
                        + "."
                        + new_format,
                    )
                    # making the directory inside the destination if not exits
                    _make_directory(new_path)

                    image.save(new_path, new_format)
            except (
                FileNotFoundError,
                UnidentifiedImageError,
                OSError,
                Exception,
            ) as error:
                print(f"An error occurred while processing {path}: {error}")

    def rotate_images(self, degrees: int) -> None:
        """
        Rotates all images in the image folder by the specified number of degrees
        and saves them to the process folder.
        """
        image_paths = self._get_all_image_paths()
        for path in image_paths:
            try:
                with Image.open(path) as image:
                    rotated_image = image.rotate(degrees, expand=True)
                    new_path = os.path.join(
                        self.process_folder, os.path.relpath(path, self.image_folder)
                    )

                    # making the directory inside the destination if not exits
                    _make_directory(new_path)

                    rotated_image.save(new_path)
            except (
                FileNotFoundError,
                UnidentifiedImageError,
                OSError,
                Exception,
            ) as error:
                print(f"An error occurred while processing {path}: {error}")

    def blur_images(self, radius: int) -> None:
        """
        Blurs all images in the image folder by the specified radius
        and saves them to the process folder.
        """
        image_paths = self._get_all_image_paths()
        for path in image_paths:
            try:
                with Image.open(path) as image:
                    blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
                    new_path = os.path.join(
                        self.process_folder, os.path.relpath(path, self.image_folder)
                    )

                    # making the directory inside the destination if not exits
                    _make_directory(new_path)

                    blurred_image.save(new_path)
            except (
                FileNotFoundError,
                UnidentifiedImageError,
                OSError,
                Exception,
            ) as error:
                print(f"An error occurred while processing {path}: {error}")

    def grayscale_images(self) -> None:
        """
        Converts all images in the image folder to grayscale
        and saves them to the process folder.
        """
        image_paths = self._get_all_image_paths()
        for path in image_paths:
            try:
                with Image.open(path) as image:
                    grayscale_image = image.convert("L")
                    new_path = os.path.join(
                        self.process_folder, os.path.relpath(path, self.image_folder)
                    )

                    # making the directory inside the destination if not exits
                    _make_directory(new_path)

                    grayscale_image.save(new_path)
            except (
                FileNotFoundError,
                UnidentifiedImageError,
                OSError,
                Exception,
            ) as error:
                print(f"An error occurred while processing {path}: {error}")
