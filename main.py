from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

from selenium.webdriver.chrome.options import Options

# Konfiguracja opcji Chrome
chrome_options = Options()
chrome_options.add_argument("user-data-dir=C://Users//USER//AppData//Local//Google//Chrome//User Data")
chrome_options.add_argument("profile-directory=Profile 1")
chrome_options.add_experimental_option('detach', True)  # Zapobiega automatycznemu zamknięciu przeglądarki

# Upewnij się, że ścieżka do chromedriver.exe jest poprawna. Jeśli plik nie znajduje się w katalogu projektu, podaj pełną ścieżkę.
driver = webdriver.Chrome(options=chrome_options)

# Otwórz stronę Tinder
driver.get('https://tinder.com/')
driver.maximize_window()


time.sleep(4)

enough_likes = True
while enough_likes:
    try:
        like_btn = driver.find_element(By.XPATH, "//span[@class='Hidden' and contains(text(),'Polub')]/ancestor::button")
        like_btn.click()
        time.sleep(2)
        continue
    except ElementClickInterceptedException:
        print('Upss Popup')
        try:
            close_btn = driver.find_element(By.CSS_SELECTOR, "button[title='Wróć do Tindera']")
            close_btn.click()
            print('Popup closed')

        except NoSuchElementException:
            print('Theres no popup button')
        try:
            super_like_btn = driver.find_element(By.XPATH, "//div[contains(text(), 'Nie, dziękuję')]")
            super_like_btn.click()
        except NoSuchElementException:
            pass


    except Exception as e:
        print(f"Inny błąd: {str(e)}")
