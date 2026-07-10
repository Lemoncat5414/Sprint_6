import allure
from data import User_1, User_2
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestScooterOrder:

    @allure.title("Оформление через кнопку Заказать в шапке")
    def test_order_up_button_user1(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.click_btn_order_up()
        order_page.complete_scooter_order(User_1)

        assert order_page.order_completed()

    @allure.title("Оформление через кнопку Заказать внизу страницы")
    def test_order_low_button_user2(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.click_btn_order_low()
        order_page.complete_scooter_order(User_2)

        assert order_page.order_completed()