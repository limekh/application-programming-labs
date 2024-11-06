import os
import csv


def read_file(annotation: str) -> list:
    """
    read rows from file and write them in massive
    :param annotation: file path
    :return: rows massive from file
    """
    if not os.path.exists(annotation):
        raise FileNotFoundError(f"Аннотация {annotation} не найдена")
    paths = []
    with open(annotation, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for line in reader:
            paths += line
    return paths
