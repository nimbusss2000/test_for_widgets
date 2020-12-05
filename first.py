# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import time

from selenium.webdriver.common.by import By

from deal import Deal


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path="/home/eugryumova/chromedriver/chromedriver")
        self.wd.implicitly_wait(30)

    
    def test_add_quick_deal(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username='eugryumova@team.amocrm.com', password='uW6OXmCqPV')
        self.create_quick_deal(wd, Deal(deal_name="testt2", contact_name="test_namet2", company_name="test_company21"))
        self.logout(wd)

    def logout(self, wd):
        time.sleep(3)
        wd.find_element(By.ID, "6469369").click()
        wd.find_element(By.LINK_TEXT, u"выйти").click()

    def create_quick_deal(self, wd, deal):
        # open deals page/ create quick deal
        time.sleep(3)
        try:
            wd.find_element(By.CSS_SELECTOR, 'div[class="pipeline_leads__quick_add_button "]').click()
        except TimeoutError as exc:
            print(f'{exc}')
            wd.find_element(By.CSS_SELECTOR, 'div[class="pipeline_leads__quick_add_button "]').click()
        # fill deal form
        wd.find_element(By.ID, "fieldname").clear()
        wd.find_element(By.ID, "fieldname").send_keys(deal.deal_name)
        wd.find_element(By.NAME, "1_fieldname").click()
        wd.find_element(By.NAME, "1_fieldname").clear()
        wd.find_element(By.NAME, "1_fieldname").send_keys(deal.contact_name)
        wd.find_element(By.NAME, "3_fieldname").click()
        wd.find_element(By.NAME, "3_fieldname").clear()
        wd.find_element(By.NAME, "3_fieldname").send_keys(deal.company_name)
        # submit deal creation
        wd.find_element(By.XPATH, "//button[@id='quick_add_form_button']/span/span").click()

    def login(self, wd, username, password):
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Логин"]').send_keys(username)
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Пароль"]').send_keys(password)
        wd.find_element(By.ID, "auth_submit").click()

    def open_home_page(self, wd):
        wd.get("https://eugryumova.amocrm.ru/")


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
