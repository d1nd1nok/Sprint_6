import allure
import pytest
from pages.faq_page import FaqPage
from scr.test_data import FAQ_DATA
from scr.config import URL


class TestFAQ:

    @allure.title("Проверка вопроса и ответа в FAQ")
    @pytest.mark.parametrize("index, exp_qu_text, exp_ans_text", FAQ_DATA)
    def test_faq_questions(self, driver, index, exp_qu_text, exp_ans_text):
        faq = FaqPage(driver)

        faq.open(URL)

        actual_text_question = faq.click_question_and_return_text(index)

        assert exp_qu_text in actual_text_question

        actual_text_answer = faq.get_answer_text(index)

        assert exp_ans_text in actual_text_answer




