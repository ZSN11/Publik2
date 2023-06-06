from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class TestLogist:
    def setup(self):
        self.user ="serg.nik.z@yandex.ru"
        self.password="123"

    def open(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://petfriends.skillfactory.ru/login")

    def close(self):
        self.driver.quit()

    def login(self):
        self.driver.find_element(By.XPATH,'//input[@id="email"]').send_keys(self.user)
        self.driver.find_element(By.XPATH,'//input[@id="pass"]').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//button[@class="btn btn-success"][text()="Войти"]').click()
        sleep(5)
        assert WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME,("h1").text)))=="PetFriends"
        #assert WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//h1[@class="text-center"][text()="PetFriends"]')))
       # self.driver.find_element(By.XPATH,'//a[@class="nav-link"][text()="Мои питомцы"]').click()


    def test_count(self):       # Проверка числинности ритомцев
        self.open()
        self.login()

        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="card-deck"]/div[@class="card"]')))
        assert len(self.driver.find_elements(By.XPATH, '//div[@class="card-deck"]/div[@class="card"]')) == 100
        self.close()


    def test_photo(self):       #Проверка, что фото имеют больше половины питомцев
        self.open()
        self.login()
        self.driver.implicitly_wait(10)
        # Определяем число питомцев
        myDunamicElement=self.driver.find_element(By.XPATH, ('//div[@class="card-deck"]/div[@class="card"]'))
        #Число питомцев без фото

        #assert len(self.driver.find_elements(By.XPATH, '//th/img[@src]'))>4





        
        
