from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DriverManager:
    def __init__(self):
        # lazy initialize the webdriver to avoid creating a browser at import time
        self.driver = None

    def get_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()
        return self.driver

    def quit_driver(self):
        if self.driver:
            try:
                self.driver.quit()
            except Exception:
                pass
            self.driver = None

    def wait_for_element_xpath(self, xpath, timeout=10):
        driver = self.get_driver()
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with xpath '{xpath}' not found within {timeout} seconds.")
            return None






