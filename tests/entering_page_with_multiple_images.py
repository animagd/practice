# -*- coding: utf-8 -*-

import unittest

from browser import Browser
from pages.open_page import OpenPage
from pages.page_with_multiple_images import PageWithMultipleImages


class EnteringPageWithMultipleImages(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()
        self.open_main_page = OpenPage(self.driver).open_page_with_multiple_images()

    def test_open_page_with_multiple_images(self):
        name_of_page = PageWithMultipleImages.name_of_page
        url = 'http://pg.edu.pl/o-uczelni/uczelnia/wladze/rektor-i-prorektorzy'

        get_page_name = self.open_main_page.take_name_of_page(name_of_page).text

        self.assertEqual(get_page_name, name_of_page)
        self.assertEqual(PageWithMultipleImages(self.driver).get_current_url(), url)

    def test_photos_are_visible(self):
        photos = ['rector_photo', 'first_vice-rector_photo', 'second_vice-rector_photo', 'third_vice-rector_photo',
                  'fourth_vice-rector_photo']

        for i in range(len(photos)):
            rector_photo_visible = PageWithMultipleImages(self.driver).checking_if_photos_is_visible(photos[i])
            self.assertEqual(rector_photo_visible, True)

        PageWithMultipleImages(self.driver).checking_response_code()

    # def tearDown(self):
    #     self.browser.stop()