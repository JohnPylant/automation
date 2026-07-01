#Login to the home page
import sys
import time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from dataSets.WebsiteUrls import WebsiteUrls
from webElements.FirstPage import FirstPage
from utils.Verifications import Verifications


website_urls = WebsiteUrls()
first_page = FirstPage()
verifications = Verifications()

class HomePageLogin:

    def load_home_page(self):
        website_urls.load_Home_url(website_urls.browser)
        website_urls.browser.maximize_window()

    def close_home_page(self, timeInSeconds):
        website_urls.close_page(timeInSeconds)

    def verify_home_button_active(self):
        home_button = verifications.verify_xpath(website_urls.browser, first_page.navigationBarElements()["homeButtonXpath"])
        if home_button.is_displayed() and home_button.is_enabled():
            print("Home button is active.")
        else:
            print("Home button is not active.")



if __name__ == "__main__":
    actions = HomePageLogin()
    actions.load_home_page()
    time.sleep(3)
    actions.verify_home_button_active()
    actions.close_home_page(3)

