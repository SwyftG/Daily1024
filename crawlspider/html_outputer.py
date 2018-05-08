#!/usr/bin/python
# -*- coding: utf-8 -*-

import time


class HtmlOutputer(object):
    def __init__(self, file_root):
        self.data = []
        self.file_root = file_root
        self.data_list = {}

    def collect_data(self, new_data):
        if new_data is None:
            return
        for item in new_data:
            if item not in self.data:
                self.data.append(item)

    def collect_data(self, name, new_data):
        if new_data is None:
            return
        temp_block = self.data_list.get(name)
        if temp_block is None:
            self.data_list[name] = new_data
        else:
            for item in new_data:
                if item not in temp_block:
                    temp_block.append(item)

    def _sort_data(self):
        for item in self.data_list:
            data = self.data_list.get(item)
            data.sort(key=lambda k: (k.post_time[-5:]), reverse=True)
            data.sort(key=lambda k: (k.post_time[0:2]))

    def output_html(self):
        self._sort_data()
        filename = self.file_root + "index.html"
        block_info = {}
        result_root_file = open(filename, 'w')
        result_root_file.write("<html>")
        result_root_file.write("<body>")
        result_root_file.write("<table>")
        result_root_file.write("<tr>")
        result_root_file.write("<h3> %s </h3>" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        result_root_file.write("</tr>")
        for item_name in self.data_list:
            item_file_url = self.file_root + item_name + ".html"
            block_info[item_name] = item_file_url
            result_root_file.write("<tr>")
            result_root_file.write("<td></td>")
            result_root_file.write("<td><a href=\"%s\" target=\"_self\"> %s </a></td>" % (item_file_url,item_name))
            result_root_file.write("</tr>")
        result_root_file.write("<style type=\"text/css\"> a:visited { color:#DC143C; text-decoration:none; } a:hover { color:#FF00FF; text-decoration:none; } a:active { color:#D200D2; text-decoration:none; } </style>")
        result_root_file.write("</table>")
        result_root_file.write("</body>")
        result_root_file.write("</html>")
        result_root_file.close()

        for block_name in block_info:
            block_data_list = self.data_list.get(block_name)
            block_file = open(block_info[block_name], 'w')
            block_file.write("<html>")
            block_file.write("<body>")
            block_file.write("<table>")
            block_file.write("<tr>")
            block_file.write("<h3> %s </h3>" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            block_file.write("</tr>")
            pre_time = ""
            block_file.write("<tr>")
            block_file.write("<td></td>")
            block_file.write("<td>**************************  %s  ****************************</td>" % block_name)
            block_file.write("</tr>")
            for data in block_data_list:
                if pre_time not in data.post_time:
                    block_file.write("<tr>")
                    block_file.write("<td></td>")
                    block_file.write("<td>******************************************************</td>")
                    block_file.write("</tr>")
                block_file.write("<tr>")
                block_file.write("<td> %s </td>" % data.post_id)
                block_file.write("<td><a href=\"%s\" target=\"_blank\"> %s </a></td>" % (data.post_url, data.post_title))
                block_file.write("<td> %s </td>" % data.post_time)
                block_file.write("<tr>")
                block_file.write("</tr>")
                pre_time = data.post_time[0:2]
            block_file.write("</table>")
            block_file.write("<style type=\"text/css\"> a:visited { color:#DC143C; text-decoration:none; } a:hover { color:#FF00FF; text-decoration:none; } a:active { color:#D200D2; text-decoration:none; } </style>")
            block_file.write("</body>")
            block_file.write("</html>")
            block_file.close()