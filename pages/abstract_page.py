# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait


class AbstractPage(object):
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