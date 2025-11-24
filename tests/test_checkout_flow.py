from pages.login_page import LoginPage

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"
PRODUCT_NAME = "Sauce Labs Backpack"


def test_complete_checkout_flow(login_page: LoginPage):
    # Login
    inventory_page = login_page.login(VALID_USER, VALID_PASSWORD)
    inventory_page.assert_logged_in()

    # Add item to cart
    inventory_page.add_item_to_cart_by_name(PRODUCT_NAME)

    # Go to cart
    cart_page = inventory_page.open_cart()
    cart_page.assert_item_in_cart(PRODUCT_NAME)

    # Checkout - information
    checkout_page = cart_page.checkout()
    overview_page = checkout_page.fill_customer_info_and_continue(
        "John", "Doe", "12345"
    )

    # Finish order
    overview_page.finish()
    overview_page.assert_order_completed()
