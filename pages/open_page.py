# -*- coding: utf-8 -*-
from dictionaries import Dictionaries
from documents_page import DocumentsPage
from pages.FAQ_page import FAQPage
from pages.abstract_page import AbstractPage
from pages.contact_page import ContactPage
from pages.eArchives_page import eArchivesPage
from pages.recruitment_page import RecruitmentPage
from pages.science_page import SciencePage
from pages.students_page import StudentsPage


class OpenPage(AbstractPage):
    def __init__(self, driver):
        super(OpenPage, self).__init__(driver)

    def open_simple_pages(self):
        self.driver.get(Dictionaries.main_pages_list['main_page'] + Dictionaries.main_pages_list['dzial_archiwum'])

    def open_page_FAQ(self):
        self.find_element(*Dictionaries.locator_dictionary['faq_page_button']).click()
        return FAQPage(self.driver)

    def open_page_eArchives(self):
        self.find_element(*Dictionaries.locator_dictionary['archives_page_button']).click()
        return eArchivesPage(self.driver)

    def open_page_documents(self):
        self.find_element(*Dictionaries.locator_dictionary['documents_page_button']).click()
        return DocumentsPage(self.driver)

    def open_page_contact(self):
        self.find_element(*Dictionaries.locator_dictionary['contact_page_button']).click()
        return ContactPage(self.driver)

    def open_complex_pages(self):
        self.driver.get(Dictionaries.main_pages_list['main_page'])

    def open_page_students(self):
        self.find_element(*Dictionaries.locator_dictionary['students_page_button']).click()
        return StudentsPage(self.driver)

    def open_page_recruitment(self):
        self.find_element(*Dictionaries.locator_dictionary['recruitment_page_button']).click()
        return RecruitmentPage(self.driver)

    def open_page_science(self):
        self.find_element(*Dictionaries.locator_dictionary['science_page_button']).click()
        return SciencePage(self.driver)