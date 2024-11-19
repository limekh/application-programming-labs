import argparse

from crop_image import crop_image
from image_size import image_size
from load_image import load_image
from plot_histogram import plot_histogram
from save_image import save_image
from show_image import show_image


def parse_arguments():
    parser = argparse.ArgumentParser(description='Image processing with OpenCV')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('-s', '--size', type=int, nargs=2,
                        help='Width and height to crop the image from the top-left corner')
    return parser.parse_args()


def main():
    args = parse_arguments()

    try:
        image = load_image(args.image_path)
        height, width = image_size(image)
        print(f'Default size of image: {height}x{width}')

        plot_histogram(image)

        cropped_image = crop_image(image, args.size)

        show_image(image, title='Original Image')
        show_image(cropped_image, title='Cropped Image')

        save_image(cropped_image)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
