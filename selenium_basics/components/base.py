
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:

    BASE_VAR = 'Base Var'

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(locator)).click()