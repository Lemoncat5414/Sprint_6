from selenium.webdriver.common.by import By


class MainPageLocators:
    BTN_ORDER_UP = (By.XPATH,
                    "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")  # Кнопка "Заказать" в шапке
    BTN_ORDER_LOW = (By.XPATH,
                     ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")  # Кнопки "Заказать" внизу страницы
    BTN_COOKIES = (By.ID, "rcc-confirm-button")  # Кнопки куки "Да, всё привыкли"

    # Вопросы
    QQ_1 = (By.ID, "accordion__heading-0")
    QQ_2 = (By.ID, "accordion__heading-1")
    QQ_3 = (By.ID, "accordion__heading-2")
    QQ_4 = (By.ID, "accordion__heading-3")
    QQ_5 = (By.ID, "accordion__heading-4")
    QQ_6 = (By.ID, "accordion__heading-5")
    QQ_7 = (By.ID, "accordion__heading-6")
    QQ_8 = (By.ID, "accordion__heading-7")

    # Ответы
    ANS_1 = (By.XPATH, ".//div[@id='accordion__panel-0']/p")
    ANS_2 = (By.XPATH, ".//div[@id='accordion__panel-1']/p")
    ANS_3 = (By.XPATH, ".//div[@id='accordion__panel-2']/p")
    ANS_4 = (By.XPATH, ".//div[@id='accordion__panel-3']/p")
    ANS_5 = (By.XPATH, ".//div[@id='accordion__panel-4']/p")
    ANS_6 = (By.XPATH, ".//div[@id='accordion__panel-5']/p")
    ANS_7 = (By.XPATH, ".//div[@id='accordion__panel-6']/p")
    ANS_8 = (By.XPATH, ".//div[@id='accordion__panel-7']/p")