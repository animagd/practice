# -*- coding: utf-8 -*-

from dictionaries import Dictionaries
from pages.FAQ_page import FAQPage
from pages.abstract_page import AbstractPage
from pages.business_card_page import BusinessCardPage
from pages.contact_page import ContactPage
from pages.documents_page import DocumentsPage
from pages.eArchives_page import eArchivesPage
from pages.employees_page import EmployeesPage
from pages.page_with_multiple_images import PageWithMultipleImages
from pages.recruitment_page import RecruitmentPage
from pages.science_page import SciencePage
from pages.students_page import StudentsPage


class OpenPage(AbstractPage):
    def __init__(self, driver):
        super(OpenPage, self).__init__(driver)

    def open_simple_pages(self):
        self.driver.get(self.main_pages_list['main_page'] + self.main_pages_list['dzial_archiwum'])

    def open_page_FAQ(self):
        self.find_element(*FAQPage.locators['faq_page_button']).click()
        return FAQPage(self.driver)

    def open_page_eArchives(self):
        self.find_element(*eArchivesPage.locators['archives_page_button']).click()
        return eArchivesPage(self.driver)

    def open_page_documents(self):
        self.find_element(*DocumentsPage.locators['documents_page_button']).click()
        return DocumentsPage(self.driver)

    def open_page_contact(self):
        self.find_element(*ContactPage.locators['contact_page_button']).click()
        return ContactPage(self.driver)

    def open_complex_pages(self):
        self.driver.get(self.main_pages_list['main_page'])

    def open_page_students(self):
        self.find_element(*Dictionaries.locator_dictionary['students_page_button']).click()
        return StudentsPage(self.driver)

    def open_page_recruitment(self):
        self.find_element(*Dictionaries.locator_dictionary['recruitment_page_button']).click()
        return RecruitmentPage(self.driver)

    def open_page_science(self):
        self.find_element(*Dictionaries.locator_dictionary['science_page_button']).click()
        return SciencePage(self.driver)

    def open_page_with_multiple_images(self):
        self.driver.get(self.main_pages_list['main_page'] + self.main_pages_list['about_university']
                        + self.main_pages_list['university'] + self.main_pages_list['authorities']
                        + self.main_pages_list['rectors_photo'])
        return PageWithMultipleImages(self.driver)

    def open_page_employees(self):
        self.find_element(*EmployeesPage.locators['employees_page_button']).click()
        return EmployeesPage(self.driver)

    def open_page_with_card(self, name):
        self.take_name_of_page(name).click()
        return BusinessCardPage(self.driver)