import cv2
import os


def get_image_info(image_path) -> tuple:
    """
    Get info of each image in folder - height, width and count of channels
    :param image_path:
    :return:
    """
    height = []
    width = []
    channel_count = []
    image_paths = [os.path.join(image_path, f) for f in os.listdir(image_path)]

    for img in image_paths:
        image = cv2.imread(img)
        height.append(image.shape[0])
        width.append(image.shape[1])
        channel_count.append(image.shape[2])

    return height, width, channel_count
