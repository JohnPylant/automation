#Login to the home page
import sys
import time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from dataSets.WebsiteUrls import WebsiteUrls


website_urls = WebsiteUrls()
class HomePageLogin:

    def load_home_page(self):
        website_urls.load_Home_url(website_urls.browser)
        website_urls.browser.maximize_window()

    def close_home_page(self, timeInSeconds):
        website_urls.close_page(timeInSeconds)



if __name__ == "__main__":
    actions = HomePageLogin()
    actions.load_home_page()
    actions.close_home_page(3)

