import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнить поле 'Имя'")
    def enter_f_name(self, name):
        self.send_keys_to_field(OrderPageLocators.FIELD_F_NAME, name)

    @allure.step("Заполнить поле 'Фамилия'")
    def enter_l_name(self, last_name):
        self.send_keys_to_field(OrderPageLocators.FIELD_L_NAME, last_name)

    @allure.step("Заполнить поле 'Адрес'")
    def set_address(self, address):
        self.send_keys_to_field(OrderPageLocators.FIELD_ADR, address)

    @allure.step("Выбрать станцию метро: {station_name}")
    def select_metro_station(self, station_name):
        self.click_on_locator(OrderPageLocators.FIELD_METRO)
        if station_name == "Бульвар Рокоссовского":
            self.click_on_locator(OrderPageLocators.MS_1)
        elif station_name == "Черкизовская":
            self.click_on_locator(OrderPageLocators.MS_2)

    @allure.step("Заполнить поле 'Телефон'")
    def enter_phone(self, phone):
        self.send_keys_to_field(OrderPageLocators.FIELD_PHONE, phone)

    @allure.step("Клик по кнопке 'Далее'")
    def click_next_button(self):
        self.click_on_locator(OrderPageLocators.BTN_NEXT)

    @allure.step("Выбор даты")
    def set_date(self):
        self.click_on_locator(OrderPageLocators.FIELD_DATA)
        self.click_on_locator(OrderPageLocators.SELECT_DATE)

    @allure.step("Выбор срока аренды")
    def set_rent_duration(self):
        self.click_on_locator(OrderPageLocators.FIELD_RENT)
        self.click_on_locator(OrderPageLocators.SELECT_RENT)

    @allure.step("Выбор цвета самоката 'Черный'")
    def select_color_black(self):
        self.click_on_locator(OrderPageLocators.BLACK_CHEKBOX)

    @allure.step("Выбор цвета самоката 'Серый'")
    def select_color_grey(self):
        self.click_on_locator(OrderPageLocators.GREY_CHEKBOX)

    @allure.step("Ввод комментария: {comment}")
    def add_comment(self, comment):
        self.send_keys_to_field(OrderPageLocators.FIELD_MSG, comment)

    @allure.step("Клик по кнопке 'Заказать'")
    def click_btn_order(self):
        self.click_on_locator(OrderPageLocators.BTN_ORDER)

    @allure.step("Подтверждение заказа")
    def click_btn_yes(self):
        self.click_on_locator(OrderPageLocators.BTN_YES)

    @allure.step("Проверка, что заказ оформлен")
    def order_completed(self):
        return self.find_and_wait_locator(OrderPageLocators.ORDER_OK).is_displayed()

    @allure.step("Полный процесс оформления заказа самоката 'Верхняя кнопка'")
    def complete_scooter_order(self, user_data):
        self.enter_f_name(user_data.f_name)  # Заполнить Имя
        self.enter_l_name(user_data.l_name)  # Заполнить фамилию
        self.set_address(user_data.adr)  # Заполнить адрес
        self.select_metro_station(user_data.ms)  # Заполнить станцию метро
        self.enter_phone(user_data.tel)  # Заполнить поле Телефон
        self.click_next_button()  # Клик на кнопку Далее
        self.set_date()  # Выбор даты
        self.set_rent_duration()  # Выбор срока аренды
        self.select_color_black()  # Выбор цвета самоката
        self.add_comment(user_data.msg)  # Ввод комментария
        self.click_btn_order()  # Клик на кнопку 'Заказать'
        self.click_btn_yes()  # Подтверждение заказа