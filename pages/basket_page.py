from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def test_guest_should_see_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "The basket isn't empty"

    def test_guest_should_see_empty_basket_message(self):
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text
        assert "Your basket is empty" in message, "The message is absent"