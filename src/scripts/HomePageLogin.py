#Login to the home page
import sys
import time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from dataSets.WebsiteUrls import WebsiteUrls
from webElements.FirstPageElements import FirstPage
from utils.Verifications import Verifications


website_urls = WebsiteUrls()
first_page = FirstPage()
verifications = Verifications()

#Variable to store the home button element
home_button = first_page.navigationBarElements()["homeButtonXpath"]

container_elements = first_page.sort_elements()["items_container_Xpath"]

class HomePageLogin:

    # Initialize the HomePageLogin class with the website URL So I can use it in the actions
    website_url = website_urls

    def load_home_page(self):
        website_urls.load_Home_url(website_urls.browser)
        website_urls.browser.maximize_window()

    def close_home_page(self, timeInSeconds):
        website_urls.close_page(timeInSeconds)

    def verify_home_button_active(self):
        verify_home_button = verifications.verify_xpath(website_urls.browser, home_button)
        if verify_home_button.is_displayed() and verify_home_button.is_enabled():
            print("Home button is active.")
        else:
            print("Home button is not active.")

    def click_name_asc_sort(self):
        name_asc_sort = first_page.sort_elements()["name_asc_option_Xpath"]
        verify_name_asc_sort = verifications.verify_click_element(website_urls.browser, name_asc_sort)
        if verify_name_asc_sort:
            print("Name Ascending sort option clicked successfully.")
        else:
            print("Name Ascending sort option is not clickable.")

    def verify_container_elements(self):
        website_urls.wait_for_xpath(container_elements, 10)
        verify_container_has_9 = verifications.verify_container_elements(website_urls.browser,container_elements)
        return print('Container has 9 elements' if verify_container_has_9 == '9' else 'Continer is not 9 elements')


if __name__ == "__main__":
    actions = HomePageLogin()
    actions.load_home_page()
    actions.website_url.wait_for_xpath(home_button, 10)
    actions.verify_home_button_active()
    actions.click_name_asc_sort()
    actions.verify_container_elements()
    actions.close_home_page(home_button)

