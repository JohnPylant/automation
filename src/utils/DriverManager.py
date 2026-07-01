from selenium import webdriver

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






