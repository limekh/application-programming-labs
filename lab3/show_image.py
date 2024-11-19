import cv2
import numpy as np


def show_image(image: np.ndarray, title: str = 'Image') -> None:
    """
    display the image with title
    :param image: image like numpy massive
    :param title: header of image
    :return:
    """
    cv2.imshow(title, image)
    cv2.waitKey(0)
