from selenium.webdriver.common.by import By


class Verifications:

    def verify_xpath(self, driver, xpath):
        return driver.find_element(By.XPATH, xpath)

    def verify_container_elements(self, driver, xpath):
        return driver.find_element(By.XPATH, xpath).get_attribute("childElementCount")

    def verify_click_element(self, driver, xpath):
        element = driver.find_element(By.XPATH, xpath)
        if element.is_displayed() and element.is_enabled():
            element.click()
            return True
        else:
            return False

