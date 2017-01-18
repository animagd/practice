# -*- coding: utf-8 -*-

import unittest

from browser import Browser
from dictionaries import Dictionaries
from pages.open_page import OpenPage


class ImportComplexPagesTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.open_main_page = OpenPage(self.driver).open_complex_pages()

    def test_open_page_Studenci(self):
        name_of_page = Dictionaries.name_of_page['students']

        open_page_students = OpenPage(self.driver).open_page_students()
        get_page_name = open_page_students.take_name_of_page(name_of_page).text

        self.assertEqual(get_page_name, name_of_page)

    def test_open_page_Rekrutacja(self):
        name_of_page = Dictionaries.name_of_page['recruitment']

        open_page_recruitment = OpenPage(self.driver).open_page_recruitment()
        get_page_name = open_page_recruitment.find_element(*Dictionaries.locator_dictionary['recruitment_page_logo']).text

        self.assertEqual(get_page_name, name_of_page)

    def test_open_page_Nauka(self):
        name_of_page = Dictionaries.name_of_page['science']

        open_page_science = OpenPage(self.driver).open_page_science()
        get_page_name = open_page_science.take_name_of_page(name_of_page).text

        self.assertEqual(get_page_name, name_of_page)

    # def tearDown(self):
        # self.browser.stop()