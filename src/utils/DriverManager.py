from selenium import webdriver
class DriverManager:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver






