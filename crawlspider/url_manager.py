#!/usr/bin/python
# -*- coding: utf-8 -*-


class UrlManager(object):
    def __init__(self):
        self.url_wrapper_list = {}
        self.new_urls = set()
        self.old_urls = set()
        self.cur_wrapper = None

    def add_new_url(self, url):
        if url is None or len(url) == 0:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        for item in self.url_wrapper_list:
            temp_data = self.url_wrapper_list.get(item)
            if temp_data.has_new_url():
                self.cur_wrapper = temp_data
                return True
        return False

    def get_new_url(self):
        if self.cur_wrapper is None:
            for item in self.url_wrapper_list:
                if self.url_wrapper_list.get(item).has_new_url():
                    self.cur_wrapper = self.url_wrapper_list.get(item)
                    return self.cur_wrapper.name, self.cur_wrapper.get_new_url()
            self.cur_wrapper = None
        else:
            temp_url = self.cur_wrapper.get_new_url()
            if temp_url is not None:
                return self.cur_wrapper.name, temp_url
            else:
                self.cur_wrapper = None
                return None, None

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def add_new_url_in_wrapper(self, name, url):
        if url is None:
            return
        temp_result = self.url_wrapper_list.get(name)
        if temp_result is None:
            wrapper_item = UrlWrapper(name)
            wrapper_item.add_new_url(url)
            self.url_wrapper_list[name] = wrapper_item
        else:
            self.url_wrapper_list.get(name).add_new_url(url)


class UrlWrapper(object):
    def __init__(self, name):
        self.name = name
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None or len(url) == 0:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def has_new_url(self):
        return len(self.new_urls) != 0