# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class ContactPage(AbstractPage):
    locators = {'text': (By.XPATH, '//*[@class="read-me journal-content-article"]//strong'),
                'contact_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/kontakt"]')}
    name_of_page = {'contact': 'Kontakt'}

    def __init__(self, driver):
        super(ContactPage, self).__init__(driver)