# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class AbstractPage(object):
    main_pages_list = {'main_page': 'http://pg.edu.pl/', 'dzial_archiwum': 'dzial-obiegu-i-archiwizacji-dokumentow/',
                       'about_university': 'o-uczelni/', 'university': 'uczelnia/', 'authorities': 'wladze/',
                       'rectors_photo': 'rektor-i-prorektorzy'}

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def take_name_of_page(self, text_in_page):
        return self.driver.find_element_by_link_text(text_in_page)

    def wait_for_element(self, *locator):
        return WebDriverWait(self.driver, 30).until(lambda self: self.find_element(*locator))

    def checking_if_there_is_any_text(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, ' '))
        except TimeoutException:
            raise Exception('Unable to find text in this element after waiting 10 seconds')