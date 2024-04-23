from selenium import webdriver
from find_element import find_element
from selenium.webdriver.common.by import By

def check_account(email, password):

    if not email or not password:
        print("E-posta ve şifre boş bırakılamaz!")
        return  # İşlemi burada durdur
    if len(password) <= 7:
        print("Şifre en az 7 karakter olmalıdır!")
        return
    
    driver = webdriver.Chrome()
    driver.get("https://panel.sellerflash.com/login")  

    username_field = find_element(driver, By.ID, 'username')
    username_field.send_keys(email)

    password_field = find_element(driver, By.ID, 'password')
    password_field.send_keys(password)

    okeyButton = find_element(driver, By.CLASS_NAME, 'p-button-label')
    okeyButton.click()

    errorLabel = find_element(driver, By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div')   

    if errorLabel:
        driver.quit()
        print('Şifre veya eposta hatalı girilmiştir. Lütfen tekrar deneyiniz.')
        return False
    else:
        driver.quit() 
        return True
    

def check_username(email, password):
    driver = webdriver.Chrome()
    driver.get("https://panel.sellerflash.com/login") 

    username_field = find_element(driver, By.ID, 'username', 1)
    username_field.send_keys(email)

    password_field = find_element(driver, By.ID, 'password', 1)
    password_field.send_keys(password)

    okeyButton = find_element(driver, By.CLASS_NAME, 'p-button-label', 1)
    okeyButton.click()

    menu_button = find_element(driver, By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div[8]/button')

    menu_button.click()

    account_button = find_element(driver, By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div[8]/ul/li[1]/button')

    account_button.click()

    user_username_field = find_element(driver, By.ID, 'firstName')

    firstname = user_username_field.get_attribute('value')

    user_surnanme_field = find_element(driver, By.ID, 'lastName')

    surname = user_surnanme_field.get_attribute('value')

    user_username = firstname + " " + surname

    account_info = find_element(driver, By.XPATH, '//*[@id="app"]/div/div/div/div[4]/div/div/div/div/div[1]/div/ul/li[2]')
    
    if account_info:
        account_info.click()
    else:
        account_info1 = find_element(driver, By.XPATH, '//*[@id="pv_id_18_1_header_action"]',1)
        if account_info1:
            account_info1.click()
        else:
            account_info2 = find_element(driver, By.XPATH, '//*[@id="pv_id_18_1_header_action"]/span[1]',1)
            if account_info2:
                account_info2.click()
            else:
                account_info3 = find_element(driver, By.XPATH, '//*[@id="pv_id_18_1_header_action"]/span[2]',1) 
                if account_info3:
                    account_info3.click()
                else:
                    print('HATA!')

    product_limit = find_element(driver, By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div[1]/div[4]/span/span/span') 

    if product_limit:
        product_limit_value = product_limit.text
        user_product_limit = find_element(driver, By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div[1]/div[5]/span/span/span',1)
        if user_product_limit:
            user_product_limit_value = user_product_limit.text
            your_product = find_element(driver, By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div/div/div/div/div[2]/div/div/div[1]/div[2]/span/span[1]',1)
            if your_product:
                your_product_value = your_product.text
            else:
                print('HATA!')
        else:
            print('HATA!')
    else:
        product_limit2 = find_element(driver, By.XPATH, '//*[@id="pv_id_19_1_content"]/div/div[1]/div[4]/span/span/span',1)
        if product_limit2:
            product_limit_value = product_limit2.text
            user_product_limit2 = find_element(driver, By.XPATH, '//*[@id="pv_id_19_1_content"]/div/div[1]/div[5]/span/span/span',1)
            if user_product_limit2:
                user_product_limit_value = user_product_limit2.text
                your_product2 = find_element(driver, By.XPATH, '//*[@id="pv_id_19_1_content"]/div/div[1]/div[2]/span/span[1]',1)
                if your_product2:
                    your_product_value = your_product2.text
                else:
                    print('HATA!')
            else:
                print('HATA!')
        else:
            product_limit3 = find_element(driver, By.XPATH, '//*[@id="pv_id_18_1_content"]/div/div[1]/div[4]/span/span/span',1)
            if product_limit3:
                product_limit_value = product_limit3.text
                user_product_limit3 = find_element(driver, By.XPATH, '//*[@id="pv_id_18_1_content"]/div/div[1]/div[5]/span/span/span',1)
                if user_product_limit3:
                    user_product_limit_value = user_product_limit3.text
                    your_product3 = find_element(driver, By.XPATH, '//*[@id="pv_id_18_1_content"]/div/div[1]/div[2]/span/span[1]',1)
                    if your_product3:
                        your_product_value = your_product3.text
                    else:
                        print('HATA!')
                else:
                    print('HATA!')
            else:
                print('HATA!')

    print(product_limit_value)
    print(user_product_limit_value)
    print(your_product_value)

    return user_username, product_limit_value, user_product_limit_value, your_product_value

