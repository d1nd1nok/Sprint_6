import allure
import pytest
from scr.test_data import ORDER_DATA
from pages.order_page import OrderPage
from scr.config import URL

from selenium.common.exceptions import TimeoutException


class TestOrder:

    @allure.title("Создание заказа")
    @pytest.mark.parametrize("data", ORDER_DATA, )
    def test_create_order(self, driver, data):

        page = OrderPage(driver)
        page.open(URL)
        page.open_order_form(data)
        page.fill_first_step(data)
        page.fill_second_step(data)

        assert page.is_order_successful()


    @allure.title("Редирект по клику на логотип Самоката")
    def test_scooter_logo_redirect(self, driver):

        page = OrderPage(driver)
        page.click_scooter_logo()

        assert page.get_current_url() == "https://qa-scooter.education-services.ru/"


    @allure.title("Редирект по клику на логотип Яндекса")
    def test_yandex_logo_redirect(self, driver):

        page = OrderPage(driver)
        current_window = page.get_current_window_handle()
        page.click_yandex_logo()
        page.wait_window_count(2)
        page.switch_to_new_window(current_window)

        try:
            page.wait_url_contains(("dzen", "yandex"), timeout=20)
        except TimeoutException:
            current = page.get_current_url()
            raise AssertionError(
                f"Timeout waiting for Yandex redirect. current_url={current}"
            )

        assert any(s in page.get_current_url().lower() for s in ("dzen", "yandex")), \
            f"Unexpected redirect URL: {page.get_current_url()}"

        

        