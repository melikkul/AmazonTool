from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element(driver, by, value, timeout=10):
    """Belirli bir elementi bulmaya çalışır ve bulunamazsa None döndürür."""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except (TimeoutException, NoSuchElementException):
        return None
    
def element_clikcable(driver, by, value, timeout=10):

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        return element
    except (TimeoutException, NoSuchElementException):
        return None