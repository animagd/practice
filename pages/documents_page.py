# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class DocumentsPage(AbstractPage):
    locators = {'text': (By.XPATH, '//*[@class="read-me journal-content-article"]//a'),
                'documents_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/dokumenty"]')}
    name_of_page = {'documents': 'Dokumenty'}

    def __init__(self, driver):
        super(DocumentsPage, self).__init__(driver)