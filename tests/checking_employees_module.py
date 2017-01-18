# -*- coding: utf-8 -*-

import unittest

from browser import Browser
from dictionaries import Dictionaries
from pages.employees_page import EmployeesPage
from pages.open_page import OpenPage


class CheckingEmployeesModule(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.open_main_page = OpenPage(self.driver).open_simple_pages()

    def test_open_page_Pracownicy(self):
        name_of_page = Dictionaries.name_of_page['employees']

        open_page_employees = OpenPage(self.driver).open_page_employees()
        get_page_name = open_page_employees.take_name_of_page(name_of_page).text

        self.assertEqual(get_page_name, name_of_page)

    def test_enter_the_card(self):
        OpenPage(self.driver).open_page_employees()
        name = EmployeesPage(self.driver).choose_employee()