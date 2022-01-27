from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


# def set_driver(driver=None):
#     if driver == None:
#         driver = webdriver.Firefox()
#     else:
#         driver = driver
#     driver.implicitly_wait(10)
#     return driver

# def wait(driver, waittime=5):
#     self.wait = WebDriverWait(self.driver, 10)


class MyDriver:
    def __init__(self, driver=None):
        self.driver = driver
        self.set_driver(driver)

    def set_driver(self):
        if not self.driver:
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)