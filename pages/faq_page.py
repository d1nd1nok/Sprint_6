from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException

from pages.base_page import BasePage

class FaqPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)


    def click_question_and_return_text(self, index):
        locator = (By.ID, f"accordion__heading-{index}")
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)
        return element.text

    def get_answer_text(self, index):
        locator = (By.ID, f"accordion__panel-{index}")
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text.strip()

    def is_answer_displayed(self, index):
        locator = (By.ID, f"accordion__panel-{index}")
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(locator)
            )
            return element.is_displayed()
        except TimeoutException:
            return False
        

        
