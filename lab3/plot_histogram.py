import cv2
import numpy as np
import matplotlib.pyplot as plt


def plot_histogram(image: np.ndarray) -> None:
    """
    make the histogram
    :param image: image like numpy massive
    :return:
    """
    color = ('b', 'g', 'r')
    plt.figure()
    for i, col in enumerate(color):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()
