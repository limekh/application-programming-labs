import argparse


def arg_parse():
    """
    parses vars from terminal
    :return: keyword for images, filename for images, filename for annotation
    """
    parser = argparse.ArgumentParser()  # создание экземпляра парсинга
    parser.add_argument('keyword', type=str, help='keyword for images')  # Keyword for icrawler
    parser.add_argument('-f', '--filename', type=str,
                        help='filename for images')  # Filename for images download with icrawler
    parser.add_argument('-a', '--annotation', type=str, help='filename for annotation')
    return parser.parse_args()  # парсинг аргументов
