
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.deal import DealHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path="/home/eugryumova/chromedriver/chromedriver")
        # self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.headless = True
        # self.wd = webdriver.Chrome(executable_path="/home/eugryumova/chromedriver/chromedriver", chrome_options=self.chrome_options)

        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.deal = DealHelper(self)

    def running_tests_in_headless_chrome(self, driver, download_dir):
        # add missing support for chrome "send_command"  to selenium webdriver
        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        command_result = driver.execute("send_command", params)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("https://eugryumova.amocrm.ru/")

    def destroy(self):
        self.wd.quit()