from telnetlib import EC

from selenium.webdriver.common.by import By

from config import url
from selenium.webdriver.support.wait import WebDriverWait


def elemrnt_has(XPATH, param):
    pass


class ShopPage():

    def __init__(self, driver):
        self.driver=driver

    def get_shops(self):
        return self.driver.find_element("xpath",'//h1[text()="Электроника"]')
        #return WebDriverWait(self.driver,10).until(elemrnt_has (By.XPATH,'//h1[text()="Электроника"]'))
