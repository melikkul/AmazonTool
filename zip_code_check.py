from selenium.webdriver.common.by import By
from find_element import find_element

def check_account(driver, log_screen):
  
    zip_button = find_element(driver, By.XPATH, '/html/body/div[1]/header/div/div[1]/div[1]/div[2]/span/a/div[2]/span[2]')
    if "New York 10001" not in zip_button.text:
        log_screen.append('----------------------MAĞAZA KONUMU KONTROL-----------------------')
        log_screen.append('Mağaza konumu kontrol ediliyor...')

        zip_button.click()
        enter_zip_code = find_element(driver, By.ID, 'GLUXZipUpdateInput')
        enter_zip_code.send_keys("10001")
        log_screen.append('Mağaza konumu değiştiriliyor...')
        apply_button = find_element(driver, By.ID, 'GLUXZipUpdate')
        apply_button.click()

        continue_button = find_element(driver, By.XPATH, '/html/body/div[6]/div/div/div[2]/span/span')
        continue_button.click()

        log_screen.append("Mağaza konumu başarıyla değiştirildi.")
    else:
        #log_screen.append("Zip code girilmiş.")
        return
