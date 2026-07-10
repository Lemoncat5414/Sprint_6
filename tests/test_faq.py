import allure
import pytest
from data import Urls, FAQ_ANS
from pages.main_page import MainPage

class TestMainPage:
    @allure.title("Проверка блока Вопросы о важном")
    @allure.description("При нажатии на вопрос - открывается ответ")
    @pytest.mark.parametrize("index, expected_text", list(enumerate(FAQ_ANS)))
    def test_faq_answers(self, driver, index, expected_text):
        main_page = MainPage(driver)
        main_page.go_to_url(Urls.PAGE_MAIN)
        main_page.expand_faq_qq(index)
        answer = main_page.get_faq_ans(index)

        assert expected_text in answer