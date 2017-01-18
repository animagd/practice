# -*- coding: utf-8 -*-

from pages.abstract_page import AbstractPage


class ContactPage(AbstractPage):
    def __init__(self, driver):
        super(ContactPage, self).__init__(driver)