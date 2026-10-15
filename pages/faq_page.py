import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException

from pages.base_page import BasePage

class FaqPage(BasePage):

    # locator templates stored as class attributes; methods format them with an index
    QUESTION = (By.ID, "accordion__heading-{}")
    ANSWER = (By.ID, "accordion__panel-{}")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Кликнуть на вопрос #{index} и получить текст")
    def click_question_and_return_text(self, index):
        locator = (self.QUESTION[0], self.QUESTION[1].format(index))
        question_text = self.get_text(locator)
        try:
            self.scroll_into_view(locator)
            self.click(locator)
        except ElementClickInterceptedException:
            self.js_click(locator)
        return question_text

    @allure.step("Получить текст ответа #{index}")
    def get_answer_text(self, index):
        locator = (self.ANSWER[0], self.ANSWER[1].format(index))
        return self.get_text(locator)

    @allure.step("Проверить отображение ответа #{index}")
    def is_answer_displayed(self, index):
        locator = (self.ANSWER[0], self.ANSWER[1].format(index))
        return self.is_displayed(locator)
        

        
