
import pytest
import allure
from scr.test_data import ORDER_DATA
from pages.order_page import OrderPage
from scr.config import URL

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

@allure.epic("QA Scooter")
@allure.feature("Order")
@allure.story("Create order and logo redirects")
class TestOrder:

    ORDER_BUTTON =[
        OrderPage.HEADER_ORDER_BUTTON,
        OrderPage.FOOTER_ORDER_BUTTON
    ]

    @pytest.mark.parametrize("btn", ORDER_BUTTON)
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_create_order(self, driver, btn, data):

        allure.dynamic.title("Create order")
        allure.dynamic.description("Parametrized test that creates an order using header/footer buttons and verifies success.")

        page = OrderPage(driver)
        page.open(URL)
        page.open_order_form(btn)
        page.fill_first_step(data)
        page.fill_second_step(data)

        assert page.is_order_successful()


    def test_scooter_logo_redirect(self, driver):
        allure.dynamic.title("Scooter logo redirect")
        allure.dynamic.description("Clicking the scooter logo in header redirects to the home page.")

        page = OrderPage(driver)
        page.click_scooter_logo()

        assert driver.current_url == "https://qa-scooter.education-services.ru/"


    def test_yandex_logo_redirect(self, driver):
        allure.dynamic.title("Yandex logo redirect")
        allure.dynamic.description("Clicking the Yandex logo opens a new tab and redirects to Yandex/Dzen.")

        page = OrderPage(driver)
        current_window = driver.current_window_handle
        page.click_yandex_logo()

        WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) > 1)

        for window in driver.window_handles:
            if window != current_window:
                driver.switch_to.window(window)
                break

        try:
            WebDriverWait(driver, 20).until(
                lambda d: any(s in d.current_url.lower() for s in ("dzen", "yandex"))
            )
        except TimeoutException:
            handles = driver.window_handles
            current = driver.current_url
            raise AssertionError(
                f"Timeout waiting for Yandex redirect. windows={handles}, current_url={current}"
            )

        assert any(s in driver.current_url.lower() for s in ("dzen", "yandex")), \
            f"Unexpected redirect URL: {driver.current_url}"

        

        