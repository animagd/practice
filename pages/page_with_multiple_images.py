# -*- coding: utf-8 -*-
from dictionaries import Dictionaries
from pages.abstract_page import AbstractPage


class PageWithMultipleImages(AbstractPage):
    def __init__(self, driver):
        super(PageWithMultipleImages, self).__init__(driver)

    def check_if_photos_is_visible(self, photo):
        photo = self.find_element(*Dictionaries.locator_dictionary[photo])
        photo_displayed = False

        if photo.is_displayed():
            photo_displayed = True

        return photo_displayed