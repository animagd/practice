# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class FAQPage(AbstractPage):
    locators = {'text': (By.XPATH, '//*[@class="read-me journal-content-article"]//p'),
                'faq_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/faq"]')}
    name_of_page = 'FAQ'


    def __init__(self, driver):
        super(FAQPage, self).__init__(driver)