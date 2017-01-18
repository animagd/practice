# -*- coding: utf-8 -*-

import unittest

from browser import Browser
from pages.open_page import OpenPage


class LoadingSimplePagesTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.open_main_page = OpenPage(self.driver).open_simple_pages()

    def test_open_page_FAQ(self):
        name_of_page = 'FAQ'

        open_page_FAQ = OpenPage(self.driver).open_page_FAQ()
        get_page_name = open_page_FAQ.take_name_of_page(name_of_page).text

        self.assertEqual(get_page_name, name_of_page)

    def test_open_page_eArchiwum(self):
        name_of_page = 'eArchiwum'

        open_page_eArchives = OpenPage(self.driver).open_page_eArchives()
        get_page_name = open_page_eArchives.take_name_of_page(name_of_page).text

        self.assertEqual(get_page_name, name_of_page)

    def test_open_page_Dokumenty(self):
        name_of_page = 'Dokumenty'

        open_page_documents = OpenPage(self.driver).open_page_documents()
        get_page_name = open_page_documents.take_name_of_page(name_of_page).text

        self.assertEqual(get_page_name, name_of_page)

    def test_open_page_Kontakt(self):
        name_of_page = 'Kontakt'

        open_page_contact = OpenPage(self.driver).open_page_contact()
        get_page_name = open_page_contact.take_name_of_page(name_of_page).text

        self.assertEqual(get_page_name, name_of_page)