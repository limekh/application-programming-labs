from icrawler.builtin import GoogleImageCrawler
import os


def image_download(keyword: str, filename: str) -> None:
    """
    download images by keyword in filename
    :param keyword: keyword for icrawler
    :param filename: path for images
    :return:
    """
    if not os.path.exists(filename):
        os.makedirs(filename)
    google_crawler = GoogleImageCrawler(storage={'root_dir': filename}, downloader_threads=5)
    google_crawler.crawl(keyword=keyword, max_num=500)
