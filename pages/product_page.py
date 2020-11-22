from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        product = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        product.click()

    def should_messages_after_adding_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESSFUL_MESSAGE), "The successful message is absent"

    def should_right_name_of_book(self):
        main_bookname = self.browser.find_element(*ProductPageLocators.MAIN_BOOKNAME).text
        basket_bookname = self.browser.find_element(*ProductPageLocators.BASKET_BOOKNAME).text
        assert main_bookname == basket_bookname, "Names are different"

    def should_right_total_price_of_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert book_price == book_basket_price, "Total price differs"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFUL_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESSFUL_MESSAGE), \
            "Success message is continiuing present, but should disappear"

