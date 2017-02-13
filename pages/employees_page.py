# -*- coding: utf-8 -*-

import random

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class EmployeesPage(AbstractPage):
    name_of_page = 'Pracownicy'
    locators = {'employee_name': (By.CSS_SELECTOR, '.name > a'),
                'employees_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/pracownicy"]'),
                'search_textbox': (By.CSS_SELECTOR, '#searchInput'), 'search-button': (By.CSS_SELECTOR, '.search-submit')}

    def __init__(self, driver):
        super(EmployeesPage, self).__init__(driver)

    def choose_employee(self):
        name = self.locators['employee_name']

        self.wait_for_element(*name)
        names = self.find_elements(*name)
        rand_name = random.choice(names)
        return rand_name.text

