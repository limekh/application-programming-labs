import cv2
import numpy as np


def load_image(image_path: str) -> np.ndarray:
    """
    load image from image_path
    :param image_path: path to image
    :return: numpy massive
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    return image
