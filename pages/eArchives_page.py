# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class eArchivesPage(AbstractPage):
    locators = {'text': (By.XPATH, '//*[@class="read-me journal-content-article"]//b'),
                'archives_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/earchiwum"]')}
    name_of_page = {'earchiwum': 'eArchiwum'}

    def __init__(self, driver):
        super(eArchivesPage, self).__init__(driver)