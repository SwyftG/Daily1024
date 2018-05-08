# encoding: utf-8
import webbrowser
from crawlspider.url_manager import UrlManager
from crawlspider.html_downloader import HtmlDownloader
from crawlspider.html_parser import HtmlParser
from crawlspider.html_outputer import HtmlOutputer


class Spider(object):
    def __init__(self, url_root, file_root, file_url, max_pages, block_info):
        self.file_root = file_root
        self.url_root = url_root
        self.file_url = file_url
        self.max_pages = max_pages
        self.block_info = block_info
        self.urls = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outputer = HtmlOutputer(file_root)

    def crawl_1024(self):
        parse_result = self.parser.get_urls(self.url_root, self.block_info)
        for item in parse_result:
            self.urls.add_new_url_in_wrapper(item, parse_result.get(item))

        while self.urls.has_new_url():
            name, url = self.urls.get_new_url()
            print("name: %s\ncraw: %s" %(name, url))
            html_cont = self.downloader.download_data(url)
            new_url, new_data = self.parser.parse(name, url, html_cont, self.max_pages)
            self.urls.add_new_url_in_wrapper(name, new_url)
            self.outputer.collect_data(name, new_data)

        self.outputer.output_html()
        webbrowser.open_new(self.file_url)
        webbrowser.get()
