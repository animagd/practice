# -*- coding: utf-8 -*-

import unittest

from browser import Browser
from pages.FAQ_page import FAQPage
from pages.contact_page import ContactPage
from pages.documents_page import DocumentsPage
from pages.eArchives_page import eArchivesPage
from pages.open_page import OpenPage


class LoadingSimplePagesTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.open_main_page = OpenPage(self.driver).open_simple_pages()

    def test_open_page_FAQ(self):
        name_of_page = FAQPage.name_of_page
        url = 'http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/faq'

        page_FAQ = OpenPage(self.driver).open_page_FAQ()
        get_page_name = page_FAQ.take_name_of_page(name_of_page).text
        page_FAQ.checking_if_there_is_any_text(FAQPage.locators['text'])

        self.assertEqual(get_page_name, name_of_page)
        self.assertEqual(FAQPage(self.driver).get_current_url(), url)

    def test_open_page_eArchiwum(self):
        name_of_page = eArchivesPage.name_of_page
        url = 'http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/earchiwum'

        page_eArchives = OpenPage(self.driver).open_page_eArchives()
        get_page_name = page_eArchives.take_name_of_page(name_of_page).text
        page_eArchives.checking_if_there_is_any_text(eArchivesPage.locators['text'])

        self.assertEqual(get_page_name, name_of_page)
        self.assertEqual(eArchivesPage(self.driver).get_current_url(), url)

    def test_open_page_Dokumenty(self):
        name_of_page = DocumentsPage.name_of_page
        url = 'http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/dokumenty'

        page_documents = OpenPage(self.driver).open_page_documents()
        get_page_name = page_documents.take_name_of_page(name_of_page).text
        page_documents.checking_if_there_is_any_text(DocumentsPage.locators['text'])

        self.assertEqual(get_page_name, name_of_page)
        self.assertEqual(DocumentsPage(self.driver).get_current_url(), url)

    def test_open_page_Kontakt(self):
        name_of_page = ContactPage.name_of_page
        url = 'http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/kontakt'

        page_contact = OpenPage(self.driver).open_page_contact()
        get_page_name = page_contact.take_name_of_page(name_of_page).text
        page_contact.checking_if_there_is_any_text(ContactPage.locators['text'])

        self.assertEqual(get_page_name, name_of_page)
        self.assertEqual(ContactPage(self.driver).get_current_url(), url)

    # def tearDown(self):
    #     self.browser.stop()