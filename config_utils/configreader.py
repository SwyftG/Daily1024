# encoding: utf-8
import json


class ConfigParams(object):
    def __init__(self, path):
        file = open(path, "r")
        file_json = json.load(file)
        self.url_root = file_json['url_root']
        self.file_root = file_json['file_dir']
        self.file_url = file_json['file_url']
        self.max_pages = file_json['max_pages']
        self.block_info = file_json['block_info']

    def __str__(self):
        return "Url_root: %s \nFile_root: %s \nFile_url: %s \nMax_pages: %s\nBlock_info: %s" % (self.url_root, self.file_root, self.file_url, self.max_pages, self.block_info)

    def get_1024_config(self):
        print(self)
        return self.url_root, self.file_root, self.file_url, self.max_pages, self.block_info
