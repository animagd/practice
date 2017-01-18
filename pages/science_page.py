# -*- coding: utf-8 -*-

from pages.abstract_page import AbstractPage


class SciencePage(AbstractPage):
    def __init__(self, driver):
        super(SciencePage, self).__init__(driver)