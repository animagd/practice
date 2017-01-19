# -*- coding: utf-8 -*-

import unittest

from browser import Browser
from pages.business_card_page import BusinessCardPage
from pages.employees_page import EmployeesPage
from pages.open_page import OpenPage


class CheckingEmployeesModule(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.open_main_page = OpenPage(self.driver).open_simple_pages()

    def test_open_page_Pracownicy(self):
        open_page_employees = OpenPage(self.driver).open_page_employees()
        name_of_page = open_page_employees.name_of_page
        get_page_name = open_page_employees.take_name_of_page(name_of_page).text

        self.assertEqual(get_page_name, name_of_page)

    def test_enter_business_card(self):
        OpenPage(self.driver).open_page_employees()
        name = EmployeesPage(self.driver).choose_employee()
        OpenPage(self.driver).open_page_with_card(name)

        choose_surname = self.spliting_data(name)
        surname_in_card = BusinessCardPage(self.driver).taking_surname_from_the_card()

        self.assertEqual(surname_in_card, choose_surname)

    def spliting_data(self, name):
        data = name.split()
        return data[-1]