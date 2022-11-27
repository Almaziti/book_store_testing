Shop: отображение страницы товара
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("almaz_0086@mail.ru")
# driver.find_element_by_id("password").send_keys("demouser123")
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_class_name("post-181").click()
# wait = WebDriverWait(driver, 10)
# heading = wait.until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "product_title.entry-title"), "HTML5 Forms"))
# print(heading)

# driver.quit()

Shop: количество товаров в категории
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("almaz_0086@mail.ru")
# driver.find_element_by_id("password").send_keys("demouser123")
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_class_name("cat-item.cat-item-19").click()
# wait = WebDriverWait(driver, 10)
# item = wait.until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cat-item.cat-item-19 .count"), "3"))
# print(item)

# driver.quit()

Shop: сортировка товаров
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("almaz_0086@mail.ru")
# driver.find_element_by_id("password").send_keys("demouser123")
# driver.find_element_by_id("menu-item-40").click()
# wait = WebDriverWait(driver, 10)
# selector = wait.until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-ordering"), "Default sorting"))
# print(selector)

# sorting = driver.find_element_by_class_name("orderby")
# select = Select(sorting)
# select.select_by_visible_text("Sort by price: high to low")

# second_selector = wait.until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "orderby"), "Sort by price: high to low"))
# print(second_selector)

# driver.quit()

Shop: отображение, скидка товара
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("almaz_0086@mail.ru")
# driver.find_element_by_id("password").send_keys("demouser123")
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_class_name("post-169").click()

# first_price = driver.find_element_by_css_selector(".price > del")
# first_price_get_text = first_price.text
# second_price = driver.find_element_by_css_selector(".price > ins")
# second_price_get_text = second_price.text
# assert first_price_get_text == "₹600.00"
# assert second_price_get_text == "₹450.00"

# wait = WebDriverWait(driver, 10)
# images = wait.until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "woocommerce-main-image")))
# images.click()
# close_images = wait.until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# close_images.click()

# driver.quit()


Shop: проверка цены в корзине
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_class_name("post-182").click()
# driver.find_element_by_class_name("single_add_to_cart_button").click()

# item = driver.find_element_by_class_name("cartcontents")
# item_text = item.text
# price = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# price_text = price.text
# assert item_text == "1 Item"
# assert price_text == "₹180.00"

# driver.find_element_by_class_name("wpmenucart-contents").click()

# wait = WebDriverWait(driver, 10)
# subtotal = wait.until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00"))
# print(subtotal)
# total = wait.until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".tax-rate .woocommerce-Price-amount"), "₹3.60"))
# print(total)
# driver.quit()


Shop: работа в корзине
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_css_selector(".post-182 .button").click()
# time.sleep(5)
# driver.find_element_by_css_selector(".post-180 .button").click()
# time.sleep(5)
# driver.find_element_by_class_name("wpmenucart-contents").click()
# time.sleep(5)
# driver.find_element_by_xpath("//a[@data-product_id='182']").click()
# driver.find_element_by_link_text("Undo?").click()

# driver.find_element_by_css_selector("tr:nth-child(1) .input-text").clear()
# driver.find_element_by_css_selector("tr:nth-child(1) .input-text").send_keys("3")
# driver.find_element_by_css_selector(".actions >  .button").click()

# value = driver.find_element_by_css_selector("tr:nth-child(1) .input-text")
# value_get_text = value.get_attribute("value")
# assert value_get_text == "3"

# time.sleep(5)
# driver.find_element_by_css_selector(".coupon >  .button").click()

# wait = WebDriverWait(driver, 10)
# error = wait.until(
#      EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))
# print(error)

# driver.quit()


Shop: покупка товара
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_css_selector(".post-182 .button").click()
# time.sleep(5)
# driver.find_element_by_class_name("wpmenucart-contents").click()

# wait = WebDriverWait(driver, 10)
# proceed = wait.until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))).click()

# link = wait.until(
#     EC.url_to_be("https://practice.automationtesting.in/checkout/"))
# print(link)

# driver.find_element_by_id("billing_first_name").send_keys("Ivan")
# driver.find_element_by_id("billing_last_name").send_keys("Ivanov")
# driver.find_element_by_id("billing_email").send_keys("Ivan@gmail.com")
# driver.find_element_by_id("billing_phone").send_keys("89213421541")

# driver.execute_script("window.scrollBy(0, 300);")
# time.sleep(3)
# driver.find_element_by_class_name("select2-container").click()
# driver.find_element_by_id("s2id_autogen1_search").send_keys("Iceland")

# driver.find_element_by_class_name("select2-result-label").click()
# driver.find_element_by_id("billing_address_1").send_keys("Moscow")
# driver.find_element_by_id("billing_postcode").send_keys("123456")
# driver.find_element_by_id("billing_city").send_keys("Moscow")
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(5)

# driver.find_element_by_css_selector(".wc_payment_method.payment_method_cheque > input").click()
# driver.find_element_by_id("place_order").click()

# title = wait.until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# print(title)

# method = wait.until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), "Check Payments"))
# print(method)
# driver.quit()