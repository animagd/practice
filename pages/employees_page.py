# -*- coding: utf-8 -*-

import random

from dictionaries import Dictionaries
from pages.abstract_page import AbstractPage


class EmployeesPage(AbstractPage):
    def __init__(self, driver):
        super(EmployeesPage, self).__init__(driver)

    def choose_employee(self):
        names = self.find_elements(*Dictionaries.locator_dictionary['employee_name'])
        rand_name = random.choice(names)

        return rand_name.text