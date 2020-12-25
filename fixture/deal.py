from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from model.deal import Deal


class DealHelper:

    def __init__(self, app):
        self.app = app

    def open_deal_page(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, 'div[class="nav__menu__item__icon  icon-leads "]').click()

    def create(self, deal):
        wd = self.app.wd
        time.sleep(1)
        self.open_deal_page()
        # create quick deal
        time.sleep(3)
        try:
            wd.find_element(By.XPATH, "//div[@id='pipeline_items__list_35986612']/div/div").click()
            time.sleep(2)
            # wd.find_element(By.CSS_SELECTOR, 'div[class="pipeline_leads__quick_add__wrapper clearfix"]').click()
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

    def delete_first_deal(self):
        wd = self.app.wd
        time.sleep(1)
        self.open_deal_page()
        wd.refresh()
        time.sleep(4)
        # choose first deal
        self.open_first_deal()
        wd.find_element(By.CSS_SELECTOR, ".card-fields__top-name-more .button-input-inner").click()
        element = wd.find_element(By.CSS_SELECTOR, ".button-input-pressed")
        actions = ActionChains(wd)
        actions.move_to_element(element).perform()
        # submit deletion
        wd.find_element(By.CSS_SELECTOR, "#card_delete .button-input__context-menu__item__text").click()
        wd.find_element(By.CSS_SELECTOR, ".modal-body__actions:nth-child(5) .button-input-inner__text").click()
        time.sleep(2)

    def open_first_deal(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//div[2]/div[2]/div/div[2]/a").click()

    def create_call_outgoing(self):
        self.open_deal_page()
        time.sleep(4)
        self.dial_the_number(number='+79771482566')
        self.open_the_created_deal()

    def open_the_created_deal(self):
        wd = self.app.wd
        self.open_first_deal()
        element = wd.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(wd)
        actions.move_to_element(element).perform()
        self.change_deal_form()
        wd.execute_script("window.scrollTo(0,0)")
        wd.find_element(By.CSS_SELECTOR, ".svg-common--arrow-left-dims").click()

    def change_deal_form(self, deal_name="test_name", email="test@mail.com", phone="89999999999"):
        wd = self.app.wd
        time.sleep(2)
        # change name
        wd.find_element(By.ID, "person_n").click()
        wd.find_element(By.ID, "person_n").click()
        wd.find_element(By.ID, "person_n").clear()
        wd.find_element(By.ID, "person_n").send_keys(deal_name)
        # change email
        wd.find_element(By.NAME, "CFV[207473]").click()
        wd.find_element(By.NAME, "CFV[207473]").send_keys(email)
        # change phone
        wd.find_element(By.NAME, "CFV[184723]").click()
        wd.find_element(By.NAME, "CFV[184723]").send_keys(phone)
        # submit
        wd.find_element(By.CSS_SELECTOR, "#save_and_close_contacts_link .button-input-inner__text").click()

    def dial_the_number(self, number):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, ".calls-list-toggler__icon").click()
        wd.find_element(By.ID, "itl_rtc__dial_btn").click()
        wd.find_element(By.CSS_SELECTOR, ".itoolabs_rtc_call__dial_display__phone").send_keys(number) # если ip телефония будет не от itoolabs - нужно поменять селектор
        self.press_the_tube()
        time.sleep(8)
        if len(wd.find_elements(By.ID, "itl_rtc__hung_up_btn")) > 1:
            self.press_the_tube()
        time.sleep(2)

    def press_the_tube(self):
        wd = self.app.wd
        wd.find_element(By.ID, "itl_rtc__hung_up_btn").click()

    def count(self):
        wd = self.app.wd
        self.open_deal_page()
        return len(wd.find_elements(By.CSS_SELECTOR, 'div[class="pipeline_leads__info"]'))

    def get_deal_list(self):
        wd = self.app.wd
        self.open_deal_page()
        all_deals = wd.find_elements(By.CSS_SELECTOR, 'div[class="pipeline_leads__info"]')
        deals_list = []
        for deal in all_deals:
            # TODO почему не берется id для new_deals?
            text = deal.find_element(By.CSS_SELECTOR, 'a[class="pipeline_leads__title-text h-text-overflow js-navigate-link"]').text
            deal_id = deal.get_attribute('id')
            id = deal_id.split('_')[1]
            deals_list.append(Deal(deal_name=text, id=id))
        return deals_list


