from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


password = "123"
user="serg.nik.z@yandex.ru"
driver=webdriver.Chrome()
driver.get("https://petfriends.skillfactory.ru/login")
driver.find_element(By.XPATH,'//input[@id="email"]').send_keys(user)
driver.find_element(By.XPATH, '//input[@id="pass"]').send_keys(password)
sleep(3)
driver.find_element(By.XPATH,'//button[@class="btn btn-success"]').click()
sleep(3)
driver.find_element(By.CLASS_NAME, 'navbar-toggler-icon').click()
driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()
sleep(5)
driver.find_element(By.XPATH,'//a[@class="nav-link"][text()="Мои питомцы"]').click()
sleep(3)

sleep(5)
