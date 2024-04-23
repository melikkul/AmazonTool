from selenium.webdriver.common.by import By
from category_find import category_finds
from find_element import find_element, element_clikcable
from zip_code_check import check_account
from selenium.webdriver.common.action_chains import ActionChains

def asin_finder(driver, location, log_screen):
    found_categories = category_finds(driver, log_screen)
    print(found_categories)
    
    for category_name, content_id in found_categories:
        log_screen.append(f"'{category_name}' kategorisi bulundu.")
        
        while True:
            # Hedef pencerenin açık olduğunu kontrol edin
            if driver.current_window_handle:
                element = element_clikcable(driver, By.XPATH, f'//*[@id="{content_id}"]/span/a')
                if element is not None:
                    #time.sleep(2)
                    element.click()
                    #time.sleep(3)
                    while True:
                        asins = find_element(driver, By.XPATH, '//div[@data-asin]')
                        
                        for asin in asins:    
                            data_asin = asin.get_attribute('data-asin')
                            if data_asin:
                                log_screen.append(data_asin)
                        
                        next_button = find_element(driver, By.XPATH, "//a[contains(@class, 's-pagination-next')]")
                        continue_button = find_element(driver, By.XPATH, "//a[contains(@class, 's-pagination-next s-pagination-disabled')]")
                        if next_button:
                            #time.sleep(2)
                            ActionChains(driver).move_to_element(next_button).click().perform()
                            # Yeni sayfanın yüklenmesini bekleyin
                            #time.sleep(3)
                        elif continue_button:
                            break
                        else:
                            log_screen.append('Son sayfaya ulaşıldı')
                            
                            break
                else:
                    log_screen.append('Element bulunamadı.')
                    break
            else:
                log_screen.append('Hedef pencere kapalı.')
                # WebDriver'ı yeniden başlatın veya başka bir eylem yapın
                break
        driver.get(location)
        check_account(driver)
