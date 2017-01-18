# -*- coding: utf-8 -*-

from pages.abstract_page import AbstractPage


class DocumentsPage(AbstractPage):
    def __init__(self, driver):
        super(DocumentsPage, self).__init__(driver)