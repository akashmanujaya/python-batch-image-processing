import os
import shutil

from batch_image_processing import ImageProcessor


def test_image_processor():
    processor = ImageProcessor("images", "processed_images")

    if os.path.exists("processed_images"):
        clear_directory("processed_images")

    # test resize_images
    processor.resize_images(100, 100)
    assert len(processor._get_all_image_paths()) == len(
        processor._get_image_paths("processed_images")
    )
    clear_directory("processed_images/")

    # test crop_images
    processor.crop_images(50, 50, 150, 150)
    assert len(processor._get_all_image_paths()) == len(
        processor._get_image_paths("processed_images")
    )
    clear_directory("processed_images")

    # test convert_images
    processor.convert_images("png")
    assert len(processor._get_all_image_paths()) == len(
        processor._get_image_paths("processed_images")
    )
    clear_directory("processed_images")

    # test rotate_images
    processor.rotate_images(90)
    assert len(processor._get_all_image_paths()) == len(
        processor._get_image_paths("processed_images")
    )
    clear_directory("processed_images")

    # test blur_images
    processor.blur_images(5)
    assert len(processor._get_all_image_paths()) == len(
        processor._get_image_paths("processed_images")
    )
    clear_directory("processed_images")

    # test grayscale_images
    processor.grayscale_images()
    assert len(processor._get_all_image_paths()) == len(
        processor._get_image_paths("processed_images")
    )
    clear_directory("processed_images")


def clear_directory(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Deleted all contents of {folder_path} successfully.")
    except Exception as e:
        print(f"Failed to delete {folder_path}. Reason: {e}")


test_image_processor()
