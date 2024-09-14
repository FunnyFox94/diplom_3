from utils import urls as url


def login_and_navigate_to_profile(login_page, main_page):
    login_page.go_to_url(url.LOGIN_PAGE_URL)
    login_page.wait_for_loading_login_page()
    login_page.auth_on_login_page()

    main_page.wait_for_account_button_loading()
    main_page.click_account_button()

def login_and_create_order(login_page, main_page):
    login_and_navigate_to_profile(login_page, main_page)
    main_page.go_to_url(url.BASE_URL)
    main_page.click_constructor_in_header()
    main_page.wait_for_loading_cards_content()
    main_page.drag_item_to_cart()
    main_page.click_order_button()
    main_page.wait_for_loading_modal_after_order()
    main_page.close_modal_after_order()
