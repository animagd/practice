# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.abstract_page import AbstractPage
import requests

class PageWithMultipleImages(AbstractPage):
    photos = ['rector', 'first_vice-rector', 'second_vice-rector', 'third_vice-rector', 'fourth_vice-rector']

    urls = ['http://pg.edu.pl/documents/10607/26bde40e-4706-449a-b00b-84ee2dd22351',
            'http://pg.edu.pl/documents/10607/d31f95b9-d212-418c-a1e0-a1735f76509a',
            'http://pg.edu.pl/documents/10607/9d10b922-92ee-41f2-af3d-76c3bd8729b5',
            'http://pg.edu.pl/documents/10607/5cadd030-285a-413c-96e5-1934fddc5a24',
            'http://pg.edu.pl/documents/10607/9d10b922-92ee-41f2-af3d-76c3bd8729b5']

    locators = {'rector_photo': (By.CSS_SELECTOR, '[src = "%s"]' % urls[0]),
                'first_vice-rector_photo': (By.CSS_SELECTOR, '[src = "%s"]' % urls[1]),
                'second_vice-rector_photo': (By.CSS_SELECTOR, '[src = "%s"]' % urls[2]),
                'third_vice-rector_photo': (By.CSS_SELECTOR, '[src = "%s"]' % urls[3]),
                'fourth_vice-rector_photo': (By.CSS_SELECTOR, '[src = "%s"]' % urls[4])}


    def __init__(self, driver):
        super(PageWithMultipleImages, self).__init__(driver)

    def checking_if_photos_is_visible(self, photo):
        photo_element = self.locators[photo]

        self.wait_for_element(*photo_element)
        photo = self.find_element(*photo_element)
        photo_displayed = False

        if photo.is_displayed():
            photo_displayed = True

        return photo_displayed

    def checking_response_code(self):
       for i in range(len(self.urls)):
            self.driver.get(self.urls[i])
            page = requests.get(self.urls[i])

            if page.status_code != 200:
                print 'Brakuje zdjęcia %s na stronie z wieloma obrazkami' % self.photos[i] + page.status_code