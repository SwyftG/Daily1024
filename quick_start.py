# encoding: utf-8
from config_utils.configreader import ConfigParams
from crawlspider.spider import Spider


def main():
    config = ConfigParams('config.json')
    url_root, file_root, file_url, max_pages, block_info = config.get_1024_config()
    spider = Spider(url_root, file_root, file_url, max_pages, block_info)
    spider.crawl_1024()


if __name__ == '__main__':
    main()
