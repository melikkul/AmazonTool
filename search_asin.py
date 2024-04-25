import pandas as pd
from selenium.webdriver.common.by import By
from category_find import category_finds
from find_element import find_element, element_clikcable
from zip_code_check import check_account
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback


def asin_finder(driver, location, log_screen):
    page = 0
    product = 0
    products = 0
    found_categories = category_finds(driver, log_screen)
    asin_list = []  # asin bilgilerini saklamak için bir liste oluşturun
    
    for category_name, content_id in found_categories:
        log_screen.append('--------------------------Ürün Kontrolü--------------------')
        log_screen.append(f"-->'{category_name}' kategorisi bulundu.")
        
        while True:
            try:
                # Hedef pencerenin açık olduğunu kontrol edin
                if driver.current_window_handle:
                    element = find_element(driver, By.XPATH, f'//*[@id="{content_id}"]/span/a')
                    if element is not None:
                        element.click()
                        while True:
                            # Tüm ilgili div öğelerini bulun
                            asins = driver.find_elements(By.XPATH, '//div[@data-asin]')
                            # Her bir div öğesinin data-asin değerini alın
                            for asin_element in asins:    
                                data_asin = asin_element.get_attribute('data-asin')
                                if data_asin:
                                    product += 1
                                    products += 1
                                    asin_list.append(data_asin)  # asin bilgilerini listeye ekleyin
                            
                            next_button = find_element(driver, By.XPATH, "//a[contains(@class, 's-pagination-next')]")
                            continue_button = find_element(driver, By.XPATH, "//a[contains(@class, 's-pagination-next s-pagination-disabled')]")
                            
                            if next_button:
                                ActionChains(driver).move_to_element(next_button).click().perform()
                                WebDriverWait(driver, 10).until(EC.presence_of_element_located())  # Bekleme ekleyin, sayfanın yenilendiğinden emin olun
                                page += 1
                            elif continue_button:
                                page += 1
                                break
                            else:
                                log_screen.append('Son sayfaya ulaşıldı')
                                break

                            log_screen.append(f'Sayfa: {page}, Ürün sayısı: {product}')
                            product = 0
                    else:
                        log_screen.append('Element bulunamadı.')
                        break
                else:
                    log_screen.append('Hedef pencere kapalı.')
                    # WebDriver'ı yeniden başlatın veya başka bir eylem yapın
                    break
            except Exception as e:
                traceback.print_exc()
                log_screen.append(f'Hata: {e}')
                log_screen.append('Hedef pencere kapalı veya URL yüklenemedi.')
                log_screen.append('Driver yeniden başlatılıyor...')
                
                # WebDriver'ı yeniden başlatın
                #driver.quit()
                #driver = initialize_driver()  # Sürücüyü yeniden başlatmak için fonksiyonunuzu kullanın

                break
        log_screen.append(f'Toplam ürün sayısı: {products}')
        driver.get(location)
        check_account(driver, log_screen)
    
    # Pandas DataFrame oluşturun ve asin bilgilerini içine ekleyin
    df = pd.DataFrame(asin_list, columns=['ASIN'])
    # DataFrame'i Excel dosyasına yazdırın
    #df.to_excel('asin_bilgileri.xlsx', index=False)

