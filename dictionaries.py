# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class Dictionaries(AbstractPage):
    main_pages_list = {'main_page': 'http://pg.edu.pl/', 'dzial_archiwum': 'dzial-obiegu-i-archiwizacji-dokumentow/'}
    pages_list = {'FAQ': 'faq', 'eArchiwum': 'earchiwum'}
    name_of_page = {'faq': 'FAQ', 'earchiwum': 'eArchiwum', 'documents': 'Dokumenty', 'contact': 'Kontakt', 'students': 'Studenci',
                    'recruitment': 'REKRUTACJA', 'science': 'Nauka'}
    locator_dictionary = {'faq_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/faq"]'),
                          'archives_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/earchiwum"]'),
                          'documents_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/dokumenty"]'),
                          'contact_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/kontakt"]'),
                          'students_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/studenci"]'),
                          'recruitment_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/rekrutacja"]'),
                          'recruitment_page_logo': (By.CSS_SELECTOR, '.site-logo-title > [title = "Rekrutacja"]'),
                          'science_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/nauka"]')}

    def __init__(self, driver):
        super(Dictionaries, self).__init__(driver)