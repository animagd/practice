# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class BusinessCardPage(AbstractPage):
    locators = {'surname': (By.CSS_SELECTOR, '.family-name')}

    def __init__(self, driver):
        super(BusinessCardPage, self).__init__(driver)

    def taking_surname_from_the_card(self):
        return self.find_element(*self.locators['surname']).text