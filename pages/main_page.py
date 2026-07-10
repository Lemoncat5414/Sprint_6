import allure
from data import Urls
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
# Локаторы для логотипов проверь: если они на главной, лучше брать из MainPageLocators, а не OrderPageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.PAGE_MAIN

    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            # Используем стандартный клик. Если куки нет - игнорируем, тест не должен падать
            self.click_on_locator(MainPageLocators.BTN_COOKIES)
        except Exception:
            pass

    @allure.step("Клик по кнопке 'Заказать' вверху страницы")
    def click_btn_order_up(self):
        self.click_on_locator(MainPageLocators.BTN_ORDER_UP)

    @allure.step("Клик по кнопке 'Заказать' внизу страницы")
    def click_btn_order_low(self):
        # Сначала скроллим, потом кликаем
        self.scroll_to_locator(MainPageLocators.BTN_ORDER_LOW)
        self.click_on_locator(MainPageLocators.BTN_ORDER_LOW)

    @allure.step("Раскрыть вопрос FAQ №{q_number}")
    def expand_faq_qq(self, q_number: int):
        questions = [
            MainPageLocators.QQ_1,
            MainPageLocators.QQ_2,
            MainPageLocators.QQ_3,
            MainPageLocators.QQ_4,
            MainPageLocators.QQ_5,
            MainPageLocators.QQ_6,
            MainPageLocators.QQ_7,
            MainPageLocators.QQ_8
        ]

        if not 0 <= q_number < len(questions):
            raise IndexError(f"Неверный индекс вопроса FAQ: {q_number}. Допустимый диапазон: 0-{len(questions) - 1}")

        locator = questions[q_number]

        # 1. Скроллим к элементу, чтобы он был в области видимости
        self.scroll_to_locator(locator)

        # 2. ВАЖНО: Кликаем через JS, чтобы обойти ошибку ElementClickInterceptedException.
        # Это решает проблему с перекрывающей картинкой /assets/scooter.png
        self.click_via_js(locator)

    @allure.step("Получить текст ответа FAQ №{ans_number}")
    def get_faq_ans(self, ans_number: int) -> str:
        answers = [
            MainPageLocators.ANS_1,
            MainPageLocators.ANS_2,
            MainPageLocators.ANS_3,
            MainPageLocators.ANS_4,
            MainPageLocators.ANS_5,
            MainPageLocators.ANS_6,
            MainPageLocators.ANS_7,
            MainPageLocators.ANS_8
        ]

        if not 0 <= ans_number < len(answers):
            raise IndexError(f"Неверный индекс ответа FAQ: {ans_number}. Допустимый диапазон: 0-{len(answers) - 1}")

        return self.get_element_text(answers[ans_number])

    @allure.step("Клик по лого 'Яндекс'")
    def click_yandex_logo(self):
        # ВНИМАНИЕ: Проверь, что локатор LOGO_YA действительно находится на Главной странице.
        # Если да, лучше перенести его в MainPageLocators и использовать здесь MainPageLocators.LOGO_YA
        self.click_on_locator(OrderPageLocators.LOGO_YA)

    @allure.step("Клик по лого 'Самокат'")
    def click_scooter_logo(self):
        # Аналогично: проверь источник локатора
        self.click_on_locator(OrderPageLocators.LOGO_SC)

    @allure.step("Проверить, что открыта страница Дзена (содержит 'dzen.ru')")
    def is_dzen_opened(self, timeout=10) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains("dzen.ru"))
            return True
        except Exception:
            return False