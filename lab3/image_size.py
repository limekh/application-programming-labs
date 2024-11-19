import numpy as np


def image_size(image: np.ndarray) -> tuple:
    """
    get image size - height and width
    :param image: image like numpy massive
    :return: tuple with size
    """
    height, width = image.shape[:2]
    return height, width
