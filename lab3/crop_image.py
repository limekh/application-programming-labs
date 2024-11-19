import numpy as np


def crop_image(image: np.ndarray, size: tuple):
    """

    :param image: image like numpy massive
    :param size: height and width of image
    :return:
    """
    if size is not None:
        width, height = size
        return image[:height, :width]  # Crop from the top-left corner
    return image
