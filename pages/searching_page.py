# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class SearchingPage(AbstractPage):
    locators = {'search_all_portals_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/wyszukiwarka/#?phrase=Olszewska&sortType=SCORE_DESC"]')}

    def __init__(self, driver):
        super(SearchingPage, self).__init__(driver)

    def searching_all_portals(self):
        self.driver.find_element(*self.locators['search_all_portals_button']).click()