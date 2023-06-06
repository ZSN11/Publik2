import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker  # генерирует случайные числа
from time import sleep


class TestLogist:
    def setup(self):
        self.user = "serg.nik.z@yandex.ru"
        self.password = "123"

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://dadata.ru/api/")

    def close(self):
        self.driver.quit()

    def login(self):
        self.driver.find_element(By.XPATH, '//*[@id="id_login-email"]').send_keys(self.user)
        self.driver.find_element(By.XPATH, '//*[@id="id_login-password"]').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//input[@class="button popup__button"][@value="Войти в систему"]').click()
        #   assert  self.driver.find_element(By.XPATH, '//a[@id="show-user-menu"]')
        assert WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="show-user-menu"]')))

    time.sleep(5)

    def test_by_login_by_button(self):
        self.open()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="signin"]'))).click()
        self.login()
        time.sleep(5)
        self.close()


    def test_registratioon(self):
        fake_email = Faker().email()
        self.open()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="signin"]'))).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-source="SIGNIN"][@class="js-show-popup"]'))).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="id_full_name"]'))).send_keys("Вася")
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="id_email"]'))).send_keys("fake_email")
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="id_password"]'))).send_keys("456")
        self.close()

    def teardown(self):
        self.close()