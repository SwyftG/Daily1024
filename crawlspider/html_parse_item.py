#!/usr/bin/python
# -*- coding: utf-8 -*-


class CaoliuItem(object):
    def __init__(self, post_title, post_url, post_time, post_id=0):
        self.post_title = post_title
        self.post_url = post_url
        self.post_time = post_time
        self.post_id = post_id
        self.download_url = None

    def __str__(self):
        return "Id: %s \nName: %s \nUrl: %s \nTime: %s \n--------------------------------------" %(self.post_id, self.post_title, self.post_url, self.post_time)

    def set_download_url(self, url):
        self.download_url = url