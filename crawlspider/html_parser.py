#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from crawlspider.html_parse_item import CaoliuItem

keywords = ['今天', '昨天', 'Top-marks']


class HtmlParser(object):
    def parse(self, page_url, html_cont, max_pages):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        url, data = self._get_titles(page_url, max_pages, soup)
        return url, data

    def parse(self, name, page_url, html_cont, max_pages):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        url, data = self._get_titles(page_url, soup, max_pages, name)
        return url, data

    def _get_titles(self, page_url, soup, max_pages=1, name=None):
        result_data = []
        post_blocks = soup.find_all(attrs={"class": "tal"})
        for item in post_blocks:
            post_parent = item.parent
            post_time = post_parent.find(attrs={"class": "s3"})
            if post_time is None:
                continue
            post_block = item.find('h3').find('a')
            post_name = post_block.text
            temp_url = post_block.get('href')
            if "tid" in temp_url:
                post_id = temp_url[-7:]
            else:
                post_id = temp_url[-12:-5]
            post_url = page_url[0:19] + temp_url
            parse_item = CaoliuItem(post_name, post_url, post_time.text, post_id)
            result_data.append(parse_item)
        page_count = int(page_url[-1:])
        if page_count < int(max_pages):
            page_count += 1
            next_url = page_url[:-1] + str(page_count)
        else:
            next_url = ""
        return next_url, result_data

    def get_urls(self, page_url, block_info):
        result_list = {}
        for block_name in block_info:
            block_url = page_url + "thread0806.php?fid=" + str(block_info[block_name]) + "&search=&page=1"
            result_list[block_name] = block_url
        return result_list


