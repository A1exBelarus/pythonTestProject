import allure
from webdriver_manager.chrome import ChromeDriverManager

from config.Config import *
from pages.LoginPage import LoginPage
from utils.DriverManager import DriverManager

driver = DriverManager.webDrvierRun(ChromeDriverManager().install())


# метод для закрытия браузера в конце тестов
def teardown_module(module):
    driver.close()


@allure.testcase("Пример теста по открытию веббраузера и запуску страницы Яндекс")
def test_open_browser():
    with allure.step("Открытие сайта Яндекс в браузере"):
        driver.get(YANDEX)
    with allure.step("Проверка тайтла"):
        assert "Яндекс" in driver.page_source


@allure.testcase("Пример сценарного теста с демонстрацией входа в личный кабинет")
def test_scenario_log_in_account():
    with allure.step("Открытие сайта tut.by в браузере"):
        driver.get(TUTBY)
    with allure.step("Вход в личный кабинет"):
        LoginPage.click_enter(driver)
    with allure.step("Ввести логин"):
        LoginPage.fill_field_login(driver, LOGIN)
    with allure.step("Ввести пароль"):
        LoginPage.fill_field_password(driver, PASSWORD)
    with allure.step("Снять галочку с чекбокса 'Запомнить'"):
        LoginPage.click_mark(driver)
    with allure.step("Нажать кнопку 'Войти'"):
        LoginPage.click_button_enter(driver)
    with allure.step("Проверить что пользователь залогинился"):
        LoginPage.checK_log_in(driver)
