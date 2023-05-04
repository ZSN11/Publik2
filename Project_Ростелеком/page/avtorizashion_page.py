from config import url
from selenium.webdriver.common.by import By
from config import locator_name,phone,password,locator_pass,locator_button,\
    locator_home,email,login,locotor_registr,locator_first_name,locator_second_name,\
    locator_reg_phone,locator_reg_pass,locator_reg_pasw,locator_reg_button,\
    locator_kod,locator_kod_email



class AvtorizashionPage():

    def __init__(self, driver):
        self.driver=driver

    def vizit(self):
        self.driver.get(url)

    def get_home(self):
        return self.driver.find_element(By.XPATH ,locator_home)

    def get_bad_pass(self):
        return self.driver.find_element(By.ID, "form-error-message")

    def get_kod(self):
        return self.driver.find_element(By.XPATH,locator_kod )

    def grt_kod_email(self):
        return self.driver.find_element(By.XPATH, locator_kod_email)


    def get_snall_pass(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Длина пароля должна быть не менее 8 символов"]')

    def get_pass_kir(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Пароль должен содержать только латинские буквы"]')


    def get_pass_different(self):
        return self.driver.find_element(By.XPATH, '//span[text()="Пароли не совпадают"]')


    def get_home_page_phone(self):
        self.driver.find_element(By.ID,locator_name ).send_keys(phone)
        self.driver.find_element(By.ID, locator_pass).send_keys(password)
        self.driver.find_element(By.ID,locator_button ).click()


    def get_pass_simple(self):
        return self.driver.find_element(By.ID, "form-error-message")

    def get_pass_str(self):
        return self.driver.find_element(By.XPATH, '//span[text()="Пароль должен содержать хотя бы одну заглавную букву"]')

    def get_pass_no_numbers(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"]')



    def get_home_page_email(self):
        self.driver.find_element(By.ID,locator_name ).send_keys(email)
        self.driver.find_element(By.ID, locator_pass).send_keys(password)
        self.driver.find_element(By.ID,locator_button ).click()


    def get_home_page_login(self):
        self.driver.find_element(By.ID,locator_name ).send_keys(login)
        self.driver.find_element(By.ID, locator_pass).send_keys(password)
        self.driver.find_element(By.ID,locator_button ).click()


    def get_bad_passw(self):
        self.driver.find_element(By.ID, locator_name).send_keys(phone)
        self.driver.find_element(By.ID, locator_pass).send_keys("Vgj10rt")
        self.driver.find_element(By.ID, locator_button).click()


    def registr_phone(self):
        self.driver.find_element(By.ID, locotor_registr).click()
        self.driver.find_element(By.XPATH,locator_first_name).send_keys("Иван")
        self.driver.find_element(By.XPATH, locator_second_name).send_keys("Иванов")
        self.driver.find_element(By.ID,locator_reg_phone).send_keys("89173564251")
        self.driver.find_element(By.ID, locator_reg_pass).send_keys("Xfgmur45")
        self.driver.find_element(By.ID, locator_reg_pasw).send_keys("Xfgmur45")
        self.driver.find_element(By.XPATH,locator_reg_button).click()


    def registr_email(self):
        self.driver.find_element(By.ID, locotor_registr).click()
        self.driver.find_element(By.XPATH,locator_first_name).send_keys("Иван")
        self.driver.find_element(By.XPATH, locator_second_name).send_keys("Иванов")
        self.driver.find_element(By.ID,locator_reg_phone).send_keys("SOS@yandex.ru")
        self.driver.find_element(By.ID, locator_reg_pass).send_keys("Xfgmur45")
        self.driver.find_element(By.ID, locator_reg_pasw).send_keys("Xfgmur45")
        self.driver.find_element(By.XPATH,locator_reg_button).click()

    def registr_email_small_pass(self):
        self.driver.find_element(By.ID, locotor_registr).click()
        self.driver.find_element(By.XPATH, locator_first_name).send_keys("Иван")
        self.driver.find_element(By.XPATH, locator_second_name).send_keys("Иванов")
        self.driver.find_element(By.ID, locator_reg_phone).send_keys("SOS@yandex.ru")
        self.driver.find_element(By.ID, locator_reg_pass).send_keys("Xfgmur")
        self.driver.find_element(By.ID, locator_reg_pasw).send_keys("Xfgmur")

    def registr_email_pass_kir(self):
        self.driver.find_element(By.ID, locotor_registr).click()
        self.driver.find_element(By.XPATH, locator_first_name).send_keys("Иван")
        self.driver.find_element(By.XPATH, locator_second_name).send_keys("Иванов")
        self.driver.find_element(By.ID, locator_reg_phone).send_keys("SOS@yandex.ru")
        self.driver.find_element(By.ID, locator_reg_pass).send_keys("Саша1234")
        self.driver.find_element(By.ID, locator_reg_pasw).send_keys("Саша1234")

    def registr_pass_different(self):
        self.driver.find_element(By.ID, locotor_registr).click()
        self.driver.find_element(By.XPATH, locator_first_name).send_keys("Иван")
        self.driver.find_element(By.XPATH, locator_second_name).send_keys("Иванов")
        self.driver.find_element(By.ID, locator_reg_phone).send_keys("89173564251")
        self.driver.find_element(By.ID, locator_reg_pass).send_keys("Xfgmur45")
        self.driver.find_element(By.ID, locator_reg_pasw).send_keys("Xfgm256j")
        self.driver.find_element(By.XPATH, locator_reg_button).click()


    def registr_pass_simple(self):
        self.driver.find_element(By.ID, locotor_registr).click()
        self.driver.find_element(By.XPATH, locator_first_name).send_keys("Иван")
        self.driver.find_element(By.XPATH, locator_second_name).send_keys("Иванов")
        self.driver.find_element(By.ID, locator_reg_phone).send_keys("89173564281")
        self.driver.find_element(By.ID, locator_reg_pass).send_keys("123456Xx")
        self.driver.find_element(By.ID, locator_reg_pasw).send_keys("123456Xx")
        self.driver.find_element(By.XPATH, locator_reg_button).click()


    def registr_pass_str(self):
        self.driver.find_element(By.ID, locotor_registr).click()
        self.driver.find_element(By.XPATH, locator_first_name).send_keys("Иван")
        self.driver.find_element(By.XPATH, locator_second_name).send_keys("Иванов")
        self.driver.find_element(By.ID, locator_reg_phone).send_keys("89173564281")
        self.driver.find_element(By.ID, locator_reg_pass).send_keys("12cfbhmx")
        self.driver.find_element(By.ID, locator_reg_pasw).send_keys("12cfbhmx")
        self.driver.find_element(By.XPATH, locator_reg_button).click()


    def registr_pass_no_numbers(self):
        self.driver.find_element(By.ID, locotor_registr).click()
        self.driver.find_element(By.XPATH, locator_first_name).send_keys("Иван")
        self.driver.find_element(By.XPATH, locator_second_name).send_keys("Иванов")
        self.driver.find_element(By.ID, locator_reg_phone).send_keys("89173564281")
        self.driver.find_element(By.ID, locator_reg_pass).send_keys("Wscfbhmx")
        self.driver.find_element(By.ID, locator_reg_pasw).send_keys("Wscfbhmx")


