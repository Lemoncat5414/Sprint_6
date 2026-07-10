import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть главную страницу")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Поиск и ожидание видимости элемента")
    def find_and_wait_locator(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание появления элемента (presence)")
    def wait_for_element(self, locator, timeout=None):
        # ИСПРАВЛЕНО: убираем двойной until и передаём таймаут корректно
        wait = WebDriverWait(self.driver, timeout or self.wait._timeout)
        return wait.until(EC.presence_of_element_located(locator))

    @allure.step("Кликнуть по элементу")
    def click_on_locator(self, locator):
        element = self.find_and_wait_locator(locator)
        element.click()

    @allure.step("Клик по элементу через JavaScript (обход перекрытия)")
    def click_via_js(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввод данных в поле")
    def send_keys_to_field(self, locator, text):
        element = self.find_and_wait_locator(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        return self.find_and_wait_locator(locator).text

    @allure.step("Скроллинг до элемента")
    def scroll_to_locator(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Плавный скролл к элементу с ActionChains")
    def scroll_and_move_to(self, locator):
        element = self.find_and_wait_locator(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step("Ожидание исчезновения элемента (например, оверлея)")
    def wait_element_disappears(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element_located(locator))

    @allure.step('Перейти на другую вкладку')
    def switch_to_next_tab(self):
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        else:
            raise RuntimeError("Нет второй вкладки для переключения")