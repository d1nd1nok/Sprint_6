from datetime import date, timedelta
import random
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):

    HEADER_ORDER_BUTTON = (By.XPATH, 
            ".//div[contains(@class, 'Header_Nav')]/button[contains(text(), 'Заказать')]")
    FOOTER_ORDER_BUTTON = (By.XPATH, 
            ".//div[contains(@class, 'Home_Finish')]/button[contains(text(), 'Заказать')]")
    NAME_INPUT = (By.XPATH, ".//input[contains(@placeholder, 'Имя')]")
    LAST_NAME_INPUT = (By.XPATH, ".//input[contains(@placeholder, 'Фамилия')]")
    ADDRESS_INPUT = (By.XPATH, ".//input[contains(@placeholder, 'Адрес')]")
    STATION_INPUT = (By.XPATH, ".//input[contains(@placeholder, 'Станция')]")
    STATION_OPTIONS = (By.XPATH, ".//button[contains(@class, 'Order_SelectOption')]")
    PHONE_INPUT = (By.XPATH, ".//input[contains(@placeholder, 'Телефон')]")
    NEXT_BUTTON = (By.XPATH, 
             ".//div[contains(@class, 'NextButton')]/button[contains(text(), 'Далее')]")
    

    DELIVERY_DATE_INPUT = (By.XPATH, ".//input[contains(@placeholder, 'Когда')]")
    DATE_30_JUNE = (
            By.XPATH,
            "//div[contains(@class,'react-datepicker__day') and @aria-label='Choose вторник, 30-е июня 2026 г.']"
        )
    RENTAL_INPUT =  (By.XPATH, ".//span[@class='Dropdown-arrow']")
    RENTAL_OPTION = (By.XPATH, ".//div[contains(@class, 'Dropdown-option') and contains(., 'сутки')]")
    COLOR_CHECKBOX = (By.XPATH, ".//label[@for='black']")
    COMMENT_INPUT = (By.XPATH, ".//input[contains(@placeholder, 'Комментарий')]")
    FORM_ORDER_BUTTON = (By.XPATH, 
             ".//button[contains(text(), 'Заказать') and contains(@class, 'Button_Middle')]")
    
    CONFIRM_ORDER_BUTTON = (By.XPATH, 
             ".//button[contains(text(), 'Да') and contains(@class, 'Button_Middle')]")
    SUCCESS_MODAL = (By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]")

    SCOOTER_LOGO = (By.XPATH, ".//img[@alt = 'Scooter']")
    YANDEX_LOGO = (By.XPATH, ".//img[@alt ='Yandex']")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)

    def open_order_form(self, button):
        element = self.wait_clickable(button)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)
    
    def fill_first_step(self, data):
        self.type(self.NAME_INPUT, data["first_name"])
        self.type(self.LAST_NAME_INPUT, data["last_name"])
        self.type(self.ADDRESS_INPUT, data["address"])
        self.wait_clickable(self.STATION_INPUT).click()
        options = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.STATION_OPTIONS)
        )
        options[0].click()
        self.type(self.PHONE_INPUT, data["phone"])
        self.wait_clickable(self.NEXT_BUTTON).click()
    
    def fill_second_step(self, data):
        self.wait_clickable(self.DELIVERY_DATE_INPUT).click()
        self.wait_clickable(self.DATE_30_JUNE).click()
        self.wait_clickable(self.RENTAL_INPUT).click()
        self.wait_clickable(self.RENTAL_OPTION).click()
        self.wait_clickable(self.COLOR_CHECKBOX).click()
        self.wait_clickable(self.COMMENT_INPUT).send_keys(data['comment'])
        self.wait_clickable(self.FORM_ORDER_BUTTON).click()
        self.wait_clickable(self.CONFIRM_ORDER_BUTTON).click()

    def is_order_successful(self):
        return self.wait_visible(self.SUCCESS_MODAL).is_displayed()




    