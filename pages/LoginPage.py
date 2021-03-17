import time

'''
Класс для работы со страницей авторизации
содержит селекторы для доступа к элементам страницы и методы по работе с ними
'''


class LoginPage:

    def click_enter(self):
        self.find_element_by_link_text('Войти').click()

    def check_mail_page(self):
        selector = '.count-me.yandex-header__logo-service.yandex-header__logo-service_lang_ru'
        self.find_element_by_css_selector(selector)
        assert "Почта" in self.title

    def fill_field_login(self, login):
        self.find_element_by_name('login').send_keys(login)

    def fill_field_password(self, password):
        self.find_element_by_name('password').send_keys(password)

    def click_mark(self):
        self.find_element_by_id('memory').click()

    def click_button_enter(self):
        self.find_element_by_css_selector("input[value='Войти']").click()

    def click_mail_button(self):
        self.find_element_by_link_text('Почта').click()
        time.sleep(3)

    def checK_log_in(self):
        assert self.find_element_by_class_name("uname")