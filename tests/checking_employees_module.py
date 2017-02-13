# -*- coding: utf-8 -*-

import unittest
from time import sleep

from hamcrest import assert_that, contains_string

from browser import Browser
from pages.business_card_page import BusinessCardPage
from pages.employees_page import EmployeesPage
from pages.open_page import OpenPage
from pages.searching_page import SearchingPage


class CheckingEmployeesModule(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.open_main_page = OpenPage(self.driver).open_simple_pages()

    def test_open_page_Pracownicy(self):
        page_employees = OpenPage(self.driver).open_page_employees()
        name_of_page = page_employees.name_of_page
        get_page_name = page_employees.take_name_of_page(name_of_page).text

        self.assertEqual(get_page_name, name_of_page)

    def test_enter_business_card(self):
        OpenPage(self.driver).open_page_employees()
        name = EmployeesPage(self.driver).choose_employee()
        OpenPage(self.driver).open_page_with_card(name)

        choose_surname = self.spliting_data(name)
        surname_in_card = BusinessCardPage(self.driver).taking_surname_from_the_card()

        self.assertEqual(surname_in_card, choose_surname)

    def test_checking_search(self):
        name = 'Olszewska'
        text_in_page = ['Wszystkie wyniki wyszukiwania dla frazy', 'Pracownicy (0']

        page_with_results = OpenPage(self.driver).open_page_with_searching_results(name)

        for i in range(len(text_in_page)):
            assert_that(page_with_results.get_page_source(), contains_string(text_in_page[i]))

        sleep(2)
        SearchingPage(self.driver).searching_all_portals()

    def spliting_data(self, name):
        data = name.split()
        return data[-1]

    # def tearDown(self):
    #     self.browser.stop()