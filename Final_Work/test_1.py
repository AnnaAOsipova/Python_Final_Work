import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import BaseApp

from testpage import OperationsHelper
import logging
import yaml, time
from selenium.webdriver.support import expected_conditions as EC

with open("testdata.yaml", encoding='utf-8') as f:
   data = yaml.safe_load(f)

name = data["username"]
passwd = data["password"]
site = data["address"]

class TestNegative:
    def test_step1(self, browser):
        logging.info("Test1 Starting")
        testpage = OperationsHelper(browser)
        testpage.go_to_site()
        testpage.enter_login("test")
        testpage.enter_pass("test")
        testpage.click_login_button()
        time.sleep(7)
        assert testpage.get_error_text() == "401"


class TestPositive:
    def test_step2(self, browser):
        logging.info("Test2 Starting")
        testpage = OperationsHelper(browser)
        testpage.enter_login(name)
        testpage.enter_pass(passwd)
        testpage.click_login_button()
        time.sleep(7)
        assert testpage.get_user_text() == f"Hello, {name}"

    def test_step3(self, browser):
        logging.info("Test3 Starting")
        testpage = OperationsHelper(browser)
        testpage.click_about_link()
        time.sleep(10)
        assert testpage.get_about_text() == "About Page"


    def test_step4(self,browser):
        logging.info("Test4 Starting")
        testpage = OperationsHelper(browser)
        assert testpage.get_about_value() == "32px", f"Expected '32px', but got '{testpage.get_about_value()}'"


