import time
from utils.DriverManager import DriverManager
driver_manager = DriverManager()
driver = driver_manager.get_driver()

class WebsiteUrls:
    browser = driver

    urlHome = "https://practicesoftwaretesting.com/"

    def load_url(self, driver, url):
        driver.get(url)

    def load_Home_url(self, driver, url = urlHome):
        driver.get(url)

    def wait_for_xpath(self, xpath, timeout=10):
        driver_manager.wait_for_element_xpath(xpath, timeout)

    def close_page(self, xpath):
        time.sleep(3)
        driver.close()




