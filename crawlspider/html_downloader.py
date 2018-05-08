#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests as request
from crawlspider.html_header import HtmlHeader


class HtmlDownloader(object):
    def __init__(self):
        self.header = HtmlHeader()

    def download_data(self, url):
        if url is None:
            return None
        head = self.header.get_header()
        result = request.get(url, headers=head, timeout=10)
        result.encoding = 'gbk'
        return result.text
