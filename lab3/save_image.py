import cv2
import numpy as np


def save_image(image: np.ndarray):
    """
    save the image
    :param image: image like numpy massive
    :return:
    """
    cv2.imwrite("cropped.jpg", image)
