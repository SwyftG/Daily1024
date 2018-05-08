#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from crawlspider.user_agents import agents


class HtmlHeader(object):
    def get_header(self):
        agent = random.choice(agents)
        return {"User-Agent": agent}
