import argparse


def parse_arguments() -> argparse.Namespace:
    """
    Parses arguments
    :return: Namespace with parsed arguments
    """
    parser = argparse.ArgumentParser(description="Process images and create annotations.")
    parser.add_argument('image_folder', type=str, help='Path to the folder with images')
    parser.add_argument('-ap', '--annotation_path', type=str, help='Path to the annotation file')
    parser.add_argument('-mh', '--max_height', type=int, help='Maximum allowed image height')
    parser.add_argument('-mw', '--max_width', type=int, help='Maximum allowed image width')
    return parser.parse_args()
