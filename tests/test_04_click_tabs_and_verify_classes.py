from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    BUNS_TAB, SAUCES_TAB, FILLINGS_TAB, PLACE_ORDER_BUTTON
)

class TestTabsNavigation:
    def test_click_tabs_and_verify_classes(self, authorized_user):
        """Проверка кликов на вкладки 'Булки', 'Соусы', 'Начинки' после авторизации."""

        wait = WebDriverWait(authorized_user, 30)

        # Проверяем успешный вход через видимость кнопки "Оформить заказ"
        assert wait.until(EC.visibility_of_element_located(PLACE_ORDER_BUTTON)), \
            "Кнопка 'Оформить заказ' не найдена, вход не удался"

        # Ожидаемый фрагмент класса, который появляется после клика
        expected_class_fragment = "tab_tab_type_current__2BEPc"

        # Клик на вкладку "Булки" и проверка класса
        authorized_user.execute_script("arguments[0].click();", wait.until(EC.element_to_be_clickable(BUNS_TAB)))
        assert expected_class_fragment in authorized_user.find_element(*BUNS_TAB).get_attribute("class")

        # Клик на вкладку "Соусы" и проверка класса
        authorized_user.execute_script("arguments[0].click();", wait.until(EC.element_to_be_clickable(SAUCES_TAB)))
        assert expected_class_fragment in authorized_user.find_element(*SAUCES_TAB).get_attribute("class")

        # Клик на вкладку "Начинки" и проверка класса
        authorized_user.execute_script("arguments[0].click();", wait.until(EC.element_to_be_clickable(FILLINGS_TAB)))
        assert expected_class_fragment in authorized_user.find_element(*FILLINGS_TAB).get_attribute("class")
