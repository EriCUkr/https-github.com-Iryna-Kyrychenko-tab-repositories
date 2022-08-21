import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestLoginPage(unittest.TestCase):


    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_sistem(self):
        user_login = TestLoginPage(self.driver)
        user_login.type_in_email('user08@getnada.com')
        user_login.type_in_passvord('Test-1234')
        user_login.click_on_the_sing_in_button()




    @classmethod
    def tearDown(self):
        self.driver.quit()