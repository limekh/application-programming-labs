import cv2
import os


def get_image_info(image_path: str) -> tuple:
    """
    Get info of each image in folder - height, width and count of channels
    :param image_path:
    :return:
    """
    img = cv2.imread(path_to_image)

    if img is None:
        raise FileNotFoundError(f"Image not found or cannot be opened: {path_to_image}")

    height, width, channels = img.shape
    return height, width, channels
