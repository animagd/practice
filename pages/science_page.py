# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class SciencePage(AbstractPage):
    name_of_page = 'Nauka'
    locators = {'science_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/nauka"]'),
                'text': (By.XPATH, '//*[@class="asset-content read-me ekontaktNews-desc news-theme-block"]//span')}

    def __init__(self, driver):
        super(SciencePage, self).__init__(driver)