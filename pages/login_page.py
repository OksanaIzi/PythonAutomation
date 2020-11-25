from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        print(login_url)
        assert "login" in login_url, "word \"login\" not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is absent"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_form.send_keys(email)
        password_form = self.browser.find_element(*LoginPageLocators.REGISTER_PASS)
        password_form.send_keys(password)
        password_form_second = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_SECOND)
        password_form_second.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()


