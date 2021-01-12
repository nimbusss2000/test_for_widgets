
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.deal import DealHelper
from selenium.webdriver.chrome.service import Service


class Application:

    def __init__(self, browser, base_url):
        self.servise = Service(executable_path='/home/eugryumova/chromedriver/chromedriver')

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-infobars")
        self.options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.notifications": 1
        })

        if browser == 'chrome':
            self.wd = webdriver.Chrome(service=self.servise, options=self.options)
        elif browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'headless_chromium':
            self.options.headless = True
            self.wd = webdriver.Chrome(service=self.servise, options=self.options)
        else:
            raise ValueError(f'unrecognized browser {browser}')
        self.wd.implicitly_wait(15)
        self.session = SessionHelper(self)
        self.deal = DealHelper(self)
        self.base_url = base_url

    def running_tests_in_headless_chrome(self, download_dir):
        # add missing support for chrome "send_command" to selenium webdriver
        wd = self.wd
        wd.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        command_result = wd.execute("send_command", params)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()