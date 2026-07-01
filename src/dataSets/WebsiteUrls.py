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

    def close_page(self, timeInSeconds):
        time.sleep(timeInSeconds)
        driver.close()




