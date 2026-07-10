from selenium.webdriver.common.by import By


class OrderPageLocators:
    # ФОРМА "Для кого самокат"
    FIELD_F_NAME = (By.XPATH, '//input[@placeholder="* Имя"]') # Поле "Имя"
    FIELD_L_NAME = (By.XPATH, '//input[@placeholder="* Фамилия"]') # Поле "Фамилия"
    FIELD_ADR = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]') # Поле "Адрес"
    FIELD_METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]') # Поле "Станция метро"
    MS_1 = (By.XPATH, '//div[text() = "Бульвар Рокоссовского"]') # Станция 1
    MS_2 = (By.XPATH, '//div[text() = "Черкизовская"]') # Станция 2
    FIELD_PHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]') # Поле "Телефон"

    BTN_NEXT = (By.XPATH, './/button[text()="Далее"]') # Кнопка "Далее"

    # Форма "Про аренду"
    FIELD_DATA = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]') # Поле "Когда привезти самокат"
    SELECT_DATE = (By.XPATH, '//div[@aria-label="Choose пятница, 31-е октября 2025 г."]') # Выбор даты
    FIELD_RENT = (By.XPATH, './/div[text()="* Срок аренды"]') # Поле "Срок аренды"
    SELECT_RENT = (By.XPATH, './/div[text()="сутки"]') # Выбор срока аренды
    BLACK_CHEKBOX = (By.ID, 'black') # Цвет - "чёрный жемчуг"
    GREY_CHEKBOX = (By.ID, 'grey') # Цвет - "серая безысходность"
    FIELD_MSG = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]') # Поле "Комментарий для курьера"

    BTN_ORDER = (By.XPATH, "(.//button[text() = 'Заказать'])[2]") # Кнопка "Заказать"

    # Окно "Хотите оформить заказ?"
    BTN_NO = (By.XPATH, './/button[text()="Нет"]') # Кнопка "Нет"
    BTN_YES = (By.XPATH, './/button[text()="Да"]') # Кнопка "Да"

   # Окно "Заказ оформлен"
    ORDER_OK = (By.XPATH, './/div[text()="Заказ оформлен"]') # Подтверждение заказа
    BTN_STATUS = (By.XPATH, './/div[text()="Посмотреть статус"]') # Кнопка "Посмотреть статус"

    # Логотипы
    LOGO_SC = (By.XPATH, ".//img[@alt='Scooter']")
    LOGO_YA = (By.XPATH, ".//img[@alt='Yandex']")