from arg_parse import arg_parse
from make_annotation import make_annotation
from image_download import image_download
from ImageIterator import ImageIterator


def main():
    args = arg_parse()
    try:
        image_download(args.keyword, args.filename)
        make_annotation(args.filename, args.annotation)
        my_iter = ImageIterator(args.annotation)
        for item in my_iter:
            print(item)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
