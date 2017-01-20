# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class Dictionaries(AbstractPage):
    # main_pages_list = {'main_page': 'http://pg.edu.pl/', 'dzial_archiwum': 'dzial-obiegu-i-archiwizacji-dokumentow/',
    #                    'about_university': 'o-uczelni/', 'university': 'uczelnia/', 'authorities': 'wladze/',
    #                    'rectors_photo': 'rektor-i-prorektorzy'}
    name_of_page = {'students': 'Studenci', 'recruitment': 'REKRUTACJA', 'science': 'Nauka', 'rectors_photo': 'Rektor i prorektorzy'}
    locator_dictionary = {'students_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/studenci"]'),
                          'recruitment_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/rekrutacja"]'),
                          'recruitment_page_logo': (By.CSS_SELECTOR, '.site-logo-title > [title = "Rekrutacja"]'),
                          'science_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/nauka"]')}

    def __init__(self, driver):
        super(Dictionaries, self).__init__(driver)