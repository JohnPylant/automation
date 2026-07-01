from selenium.webdriver.common.by import By


class Verifications:

    def verify_xpath(self, driver, xpath):
        return driver.find_element(By.XPATH, xpath)




