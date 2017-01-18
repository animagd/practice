# -*- coding: utf-8 -*-

from pages.abstract_page import AbstractPage


class StudentsPage(AbstractPage):
    def __init__(self, driver):
        super(StudentsPage, self).__init__(driver)