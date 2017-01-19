# -*- coding: utf-8 -*-

import random

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class EmployeesPage(AbstractPage):
    name_of_page = 'Pracownicy'
    locators = {'employee_name': (By.CSS_SELECTOR, '.name > a')}

    def __init__(self, driver):
        super(EmployeesPage, self).__init__(driver)

    def choose_employee(self):
        name = self.locators['employee_name']

        self.wait_for_element(*name)
        names = self.find_elements(*name)
        rand_name = random.choice(names)
        return rand_name.text