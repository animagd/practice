# -*- coding: utf-8 -*-

from selenium import webdriver


class Browser:
    def __init__(self):
        self.driver = None
        self.profile = None

    def start(self):
        self.driver = webdriver.Chrome('C:/python/chromedriver.exe')
        #self.driver.get('https://pg.edu.pl/')
        self.driver.maximize_window()
        return self.driver

    def stop(self):
        self.driver.close()