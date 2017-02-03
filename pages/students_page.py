# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class StudentsPage(AbstractPage):
    name_of_page = 'Studenci'
    locators = {'students_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/studenci"]'),
                'text': (By.XPATH, '//*[@class="asset-content read-me ekontaktNews-desc news-theme-block"]//span')}

    def __init__(self, driver):
        super(StudentsPage, self).__init__(driver)