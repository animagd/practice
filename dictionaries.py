# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage


class Dictionaries(AbstractPage):
    main_pages_list = {'main_page': 'http://pg.edu.pl/', 'dzial_archiwum': 'dzial-obiegu-i-archiwizacji-dokumentow/',
                       'about_university': 'o-uczelni/', 'university': 'uczelnia/', 'authorities': 'wladze/',
                       'rectors_photo': 'rektor-i-prorektorzy'}
    name_of_page = {'faq': 'FAQ', 'earchiwum': 'eArchiwum', 'documents': 'Dokumenty', 'contact': 'Kontakt', 'students': 'Studenci',
                    'recruitment': 'REKRUTACJA', 'science': 'Nauka', 'rectors_photo': 'Rektor i prorektorzy',
                    'employees': 'Pracownicy'}
    locator_dictionary = {'faq_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/faq"]'),
                          'archives_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/earchiwum"]'),
                          'documents_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/dokumenty"]'),
                          'contact_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/kontakt"]'),
                          'students_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/studenci"]'),
                          'recruitment_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/rekrutacja"]'),
                          'recruitment_page_logo': (By.CSS_SELECTOR, '.site-logo-title > [title = "Rekrutacja"]'),
                          'science_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/nauka"]'),
                          'rector_photo': (By.CSS_SELECTOR, '[src = "http://pg.edu.pl/documents/10607/26bde40e-4706-449a-b00b-84ee2dd22351"'),
                          'first_vice-rector_photo': (By.CSS_SELECTOR, '[src = "http://pg.edu.pl/documents/10607/d31f95b9-d212-418c-a1e0-a1735f76509a"'),
                          'second_vice-rector_photo': (By.CSS_SELECTOR, '[src = "http://pg.edu.pl/documents/10607/9d10b922-92ee-41f2-af3d-76c3bd8729b5"'),
                          'third_vice-rector_photo': (By.CSS_SELECTOR, '[src = "http://pg.edu.pl/documents/10607/9d10b922-92ee-41f2-af3d-76c3bd8729b5"'),
                          'fourth_vice-rector_photo': (By.CSS_SELECTOR, '[src = "http://pg.edu.pl/documents/10607/9d10b922-92ee-41f2-af3d-76c3bd8729b5"'),
                          'employees_page_button': (By.CSS_SELECTOR, '[href = "http://pg.edu.pl/dzial-obiegu-i-archiwizacji-dokumentow/pracownicy"]'),
                          'employee_name': (By.CSS_SELECTOR, '.name > a')}

    def __init__(self, driver):
        super(Dictionaries, self).__init__(driver)