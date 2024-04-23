import pandas as pd
from selenium import webdriver
from find_element import find_element, element_clikcable    
from selenium.webdriver.common.by import By
from zip_code_check import check_account
from category_find  import category_find, product_count, category_finds
from search_asin import asin_finder
import time

def asin_scan_fnc(location, log_screen, yukleme_ekrani):
    df = pd.read_excel(location, header=None)
    driver = webdriver.Chrome()

    # Iterate over the values in the first column
    for asin in df[0]:
        # Your logic here
        print(asin)  # For demonstration, printing each value

        driver.get(asin)
        while True:
            error_page = find_element(driver, By.XPATH, '/html/body/div/div/a/img')
            if error_page:
                driver.refresh()
            else:
                break
    check_account(driver, log_screen)
    try:
        category_all = element_clikcable(driver, By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[1]/span[1]')
        if category_all:
            category_all.click()
        else:
            print('HATA!')
    except Exception:
        print('HATA')
    time.sleep(1)
    category_find(driver, log_screen)
    time.sleep(1)
    product_count(driver, log_screen, yukleme_ekrani)  # <--- Burada log_screen parametresini ekleyin
    time.sleep(1)
    asin_finder(driver, location, log_screen)
