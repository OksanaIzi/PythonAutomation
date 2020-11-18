from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('promo', ["0","1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail(reason="some bug")), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    time.sleep(3)
    product_page.should_messages_after_adding_to_basket()
    product_page.should_right_name_of_book()
    product_page.should_right_total_price_of_basket()





