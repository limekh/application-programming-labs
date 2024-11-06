import os
import csv


def make_annotation(filename: str, annotation: str) -> None:
    """
    Create annotation file with absolute and relative paths
    :param filename: directory with images
    :param annotation: annotation path
    :return:
    """
    with open(annotation, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for f in os.listdir(filename):
            writer.writerows([[os.path.abspath(os.path.join(filename, f))],
                              [os.path.relpath(os.path.join(filename, f), start=os.curdir)]])
