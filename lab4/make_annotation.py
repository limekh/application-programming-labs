import csv
import os


def make_annotation(filename: str, annotation: str) -> None:
    """
    Create annotation file with absolute and relative paths
    :param filename: directory with images
    :param annotation: annotation path
    :return:
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Directory not found: {filename}")

    with open(annotation, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        for image in os.listdir(filename):
            absolute_path = os.path.abspath(os.path.join(filename, image))
            relative_path = os.path.relpath(absolute_path)
            writer.writerow([absolute_path, relative_path])
