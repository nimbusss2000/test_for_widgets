from selenium.webdriver.common.by import By
import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Логин"]').send_keys(username)

        wd.find_element(By.CSS_SELECTOR, 'input[placeholder="Пароль"]').send_keys(password)

        wd.find_element(By.ID, "auth_submit").click()

    def logout(self):
        wd = self.app.wd
        time.sleep(3)
        wd.find_element(By.ID, "6469369").click()
        time.sleep(1)
        wd.find_element(By.LINK_TEXT, u"выйти").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.ID, "6469369")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        wd.find_element(By.ID, "6469369").click()
        wd.find_element(By.CSS_SELECTOR,
                                 ".nav__top__userbar__profile > .nav__top__userbar__profile__text").click()
        return wd.find_element(By.NAME, "LOGIN").text == username

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

