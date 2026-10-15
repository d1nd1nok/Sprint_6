import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент {locator}")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator):
        el = self.wait_clickable(locator)
        el.click()

    @allure.step("Ввести текст '{text}' в поле {locator}")
    def type(self, locator, text):
        el = self.find(locator)
        el.send_keys(text)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить текущий window handle")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Получить все window handles")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Ожидать {count} окон")
    def wait_window_count(self, count, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) == count
        )

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, old_window_handle):
        handles = [h for h in self.get_window_handles() if h != old_window_handle]
        if not handles:
            raise RuntimeError("No new window handle found")
        self.driver.switch_to.window(handles[0])
        return handles[0]

    @allure.step("Ожидать URL содержащий {substrings}")
    def wait_url_contains(self, substrings, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: any(s in d.current_url.lower() for s in substrings)
        )

    @allure.step("Ожидать видимость всех элементов {locator}")
    def wait_all_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    @allure.step("Ожидать видимость элемента {locator}")
    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидать кликабельность элемента {locator}")
    def wait_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидать присутствие элемента {locator}")
    def wait_presence(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Ожидать исчезновение элемента {locator}")
    def wait_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Прокрутить к элементу {locator}")
    def scroll_into_view(self, locator, timeout=10, block='center'):
        el = self.wait_presence(locator, timeout)
        self.driver.execute_script(f"arguments[0].scrollIntoView({{block: '{block}'}});", el)
        return el

    @allure.step("Кликнуть через JS на элемент {locator}")
    def js_click(self, locator, timeout=10):
        el = self.wait_presence(locator, timeout)
        self.driver.execute_script("arguments[0].click();", el)
        return el

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator, timeout=10):
        el = self.wait_visible(locator, timeout)
        return el.text.strip()

    @allure.step("Проверить отображение элемента {locator}")
    def is_displayed(self, locator, timeout=5):
        try:
            el = self.wait_presence(locator, timeout)
            return el.is_displayed()
        except Exception:
            return False
