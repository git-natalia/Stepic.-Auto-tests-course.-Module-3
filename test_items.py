import time

def test_guest_should_see_button_add_to_basket(browser):
    browser.implicitly_wait(5)
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    #time.sleep(30) # для проверки работы теста с параметром --language=fr (фраза на кнопке "Ajouter au panier")
     
    button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert button, f"Button add to basket is not found"