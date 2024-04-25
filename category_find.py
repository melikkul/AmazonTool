from find_element import find_element, element_clikcable
from selenium.webdriver.common.by import By
import re
import time
from zip_code_check import check_account

categories = {
        "Appliances":"n/2619525011",
        "Arts, Crafts & Sewing": "n/2617941011",
        "Automotive": "n/15684181",
        "Baby Product": "n/165796011",
        "Beauty & Personal Care": "n/3760911",
        "Books": "n/283155",
        "CDs & Vinyl": "n/5174",
        "Cell Phones & Accessories": "n/2335752011",
        "Clothing, Shoes & Jewelry": "n/7141123011",
        "Electronics": "n/172282",
        "Everything Else": "n/10272111",
        "Grocery & Gourmet Food": "n/16310101",
        "Health & Household": "n/3760901",
        "Home & Business Services": "n/8098158011",
        "Home & Kitchen": "n/1055398",
        "Industrial & Scientific": "n/16310091",
        "Musical Instruments": "n/11091801",
        "Office Products": "n/1064954",
        "Patio, Lawn & Garden": "n/2972638011",
        "Pet Supplies": "n/2619533011",
        "Sports & Outdoors": "n/3375251",
        "Tools & Home Improvement": "n/228013",
        "Toys & Games": "n/165793011",
        "Video Games": "n/468642"
    }
count_productss = 0
found_categories = []
def category_find(driver, log_screen):
    global count_productss
    count_productss = 0
    log_screen.append('----------------------KATEGORİLER KONTROL-----------------------')
    log_screen.append('Kategoriler kontrol ediliyor...')
    for category_name, content_id in categories.items():
        element = find_element(driver, By.XPATH, f'//*[@id="{content_id}"]', 2)
        if element is not None:
            #print(f"'{category_name}' kategorisi bulundu.")
            log_screen.append(f"->'{category_name}' kategorisi bulundu.")
            found_categories.append((category_name, content_id))
            count_productss += 1
        else:
            #print(f"'{category_name}' kategorisi bulunamadı.")
            continue
    
    #print(f"{count} kategoriler bulundu.")
    log_screen.append(f"SONUÇ: {count_productss} kategoriler bulundu.") 
    
def product_count(driver,log_screen, yukleme_ekrani):
    log_screen.append('----------------------ÜRÜNLER SAYISI KONTROL-----------------------')
    global count_productss
    count_products = 0
    count_process = 0
    error_occurred = True
    log_screen.append('Ürünler sayısı kontrol ediliyor...')
    for category_name, content_id in found_categories: 
        while error_occurred:
            try:
                category_all = element_clikcable(driver, By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[1]/span[1]')
                if category_all:
                    category_all.click()
                else:
                    error_occurred = False
                    break
            except Exception:
                break
        #print(f"Kategori Adı: {category_name}, İçerik Kimliği: {content_id}")
        element = find_element(driver, By.XPATH, f'//*[@id="{content_id}"]/span/a')
        
        #print(element.text)
        
        if element is not None:
            time.sleep(2)
            element.click()
            text = find_element(driver, By.XPATH, '//*[@id="search"]/span[2]/div/h1/div/div[1]/div/div/span')
            match = re.search(r'\b\d+\b(?=\D*$)', text.text)

            if match:
                number = match.group()
                #print(type(number))
                if number == '000':
                    match2 = re.finditer(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b', text.text)
                    count = 0
                    for m in match2:
                        count += 1
                        if count == 3:
                            num = m.group()
                            count_products += int(num.replace(",", ""))
                            count_process += 1
                            calculate = (100/count_productss)* count_process
                            #print("Bulunan sayı:", num)
                            yukleme_ekrani.setValue(int(calculate))
                            log_screen.append(f"->{category_name} kategorisinde bulunan ürün: {num}")
                else:
                    count_products += int(number)
                    count_process += 1
                    calculate = (100/count_productss)* count_process
                    yukleme_ekrani.setValue(int(calculate))
                    #print("Bulunan sayı:", number)
                    log_screen.append(f"->{category_name} kategorisinde bulunan ürün: {number}")
                calculate = (100/count_productss)* count_process
                driver.back()
                time.sleep(2)
            else:
                log_screen.append("Sayı bulunamadı.")
                break
                #print("Sayı bulunamadı.")
            check_account(driver, log_screen)
        else:
            log_screen.append(f"'{category_name}' kategorisi bulunamadı.")
            #print(f"'{category_name}' kategorisi bulunamadı.")
            continue
    
    log_screen.append(f'Toplam ürün sayısı: {count_products}')
            

def category_finds(driver, log_screen):
    global count_productss
    count_productss = 0
    for category_name, content_id in categories.items():
        element = find_element(driver, By.XPATH, f'//*[@id="{content_id}"]')
        if element is not None:
            found_categories.append((category_name, content_id))
            count_productss += 1
        else:
            #print(f"'{category_name}' kategorisi bulunamadı.")
            continue
    
    #print(f"{count} kategoriler bulundu.")
    log_screen.append(f"SONUÇ: {count_productss} kategoriler bulundu.") 
    return found_categories