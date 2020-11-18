from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    time.sleep(15)
    product_page.should_messages_after_adding_to_basket()
    product_page.should_right_name_of_book()
    product_page.should_right_total_price_of_basket()





