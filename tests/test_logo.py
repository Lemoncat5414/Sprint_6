import allure
from data import Urls
from pages.main_page import MainPage


class TestLogo:

    @allure.title("Проверка перехода на главную страницу по логотипу 'Самокат'")
    def test_click_sc_logo_redirects_main(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.go_to_url(Urls.PAGE_ORDER)
        main_page.click_scooter_logo()

        assert Urls.PAGE_MAIN in main_page.get_current_url()

    @allure.title("Проверка перехода на страницу 'Dzen' по логотипу 'Яндекс'")
    def test_click_ya_logo_redirects_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_yandex_logo()
        main_page.switch_to_next_tab()

        assert main_page.is_dzen_opened()
