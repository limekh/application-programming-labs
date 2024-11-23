import cv2
import numpy as np
import matplotlib.pyplot as plt


def create_histogram(image: np.ndarray) -> dict:
    """
    create the histogram
    :param image: image like numpy massive
    :return: dict with hists for colors
    """

    hist = {}
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist[col] = cv2.calcHist([image], [i], None, [256], [0, 256])

    return hist


def show_histogram(hist: dict) -> None:
    """
    display histogram
    :param hist: dict with hists for colors
    :return:
    """
    
    plt.figure()
    for col in hist.keys():
        plt.plot(hist[col], color=col)
        plt.xlim([0, 256])

    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()
