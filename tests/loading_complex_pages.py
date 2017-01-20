# -*- coding: utf-8 -*-

import unittest

from browser import Browser
from pages.open_page import OpenPage
from pages.recruitment_page import RecruitmentPage
from pages.science_page import SciencePage
from pages.students_page import StudentsPage


class ImportComplexPagesTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.open_main_page = OpenPage(self.driver).open_complex_pages()

    def test_open_page_Studenci(self):
        name_of_page = StudentsPage.name_of_page['students']

        page_students = OpenPage(self.driver).open_page_students()
        get_page_name = page_students.take_name_of_page(name_of_page).text
        page_students.checking_if_there_is_any_text(StudentsPage.locators['text'])

        self.assertEqual(get_page_name, name_of_page)

    def test_open_page_Rekrutacja(self):
        name_of_page = RecruitmentPage.name_of_page['recruitment']

        page_recruitment = OpenPage(self.driver).open_page_recruitment()
        get_page_name = page_recruitment.find_element(*RecruitmentPage.locators['recruitment_page_logo']).text
        page_recruitment.checking_if_there_is_any_text(RecruitmentPage.locators['text'])

        self.assertEqual(get_page_name, name_of_page)

    def test_open_page_Nauka(self):
        name_of_page = SciencePage.name_of_page['science']

        page_science = OpenPage(self.driver).open_page_science()
        get_page_name = page_science.take_name_of_page(name_of_page).text
        page_science.checking_if_there_is_any_text(SciencePage.locators['text'])

        self.assertEqual(get_page_name, name_of_page)

    # def tearDown(self):
        # self.browser.stop()