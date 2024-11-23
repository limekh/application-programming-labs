import cv2
import numpy as np


def save_image(output_path: str, image: np.ndarray):
    """
    save the image
    :param output_path: path for saving
    :param image: image like numpy massive
    :return:
    """
    cv2.imwrite(output_path, image)
