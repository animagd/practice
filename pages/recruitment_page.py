# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class RecruitmentPage(AbstractPage):
    name_of_page = 'REKRUTACJA'
    locators = {'recruitment_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/rekrutacja"]'),
                'recruitment_page_logo': (By.CSS_SELECTOR, '.site-logo-title > [title = "Rekrutacja"]'),
                'text': (By.XPATH, '//*[@class= "asset-content read-me"]//a')}

    def __init__(self, driver):
        super(RecruitmentPage, self).__init__(driver)

    def get_name_of_page(self):
        return self.find_element(*self.locators['recruitment_page_logo']).text