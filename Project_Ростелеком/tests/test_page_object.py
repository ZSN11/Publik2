from page.avtorizashion_page import AvtorizashionPage
from page.shop_page import ShopPage

from time import sleep



#Авторизации по телефону ипаролю
def test_home_page_phone(driver):
    avtor_page=AvtorizashionPage(driver)
    avtor_page.vizit()
    avtor_page.get_home_page_phone()
    assert avtor_page.get_home().is_displayed() #Проверка что зашли в личный кабинет


#Авторизация по email
def test_home_page_email(driver):
    avtor_page=AvtorizashionPage(driver)
    avtor_page.vizit()
    avtor_page.get_home_page_email()
    assert avtor_page.get_home().is_displayed() #Проверка что зашли в личный кабинет

#Авторизация по login
def test_home_page_login(driver):
    avtor_page = AvtorizashionPage(driver)
    avtor_page.vizit()
    avtor_page.get_home_page_login()
    assert avtor_page.get_home().is_displayed()  # Проверка что зашли в личный кабинет

#Авторизация с неактуальным паролем
def test_bad_pass(driver):
    avtor_page = AvtorizashionPage(driver)
    avtor_page.vizit()
    avtor_page.get_bad_passw()
    # Проверяем, что вышло сообщение "Неверный логин или пароль"
    assert avtor_page.get_bad_pass().is_displayed()

#Регистрация пр номеру телефона
def test_reg_phone(driver):
    avtor_page = AvtorizashionPage(driver)
    avtor_page.vizit()
    avtor_page.registr_phone()
    #Проверяем, что призошёл переход на страницу ввода кода
    assert avtor_page.get_kod().is_displayed()


#Регистрация пр email
def test_reg_mail(driver):
    avtor_page = AvtorizashionPage(driver)
    avtor_page.vizit()
    avtor_page.registr_email()
    #Проверяем, что призошёл переход на страницу ввода кода
    assert avtor_page.grt_kod_email().is_displayed()


#Регистрация с паролем < 8 символов
def test_reg_small_pass(driver):
    avtor_page = AvtorizashionPage(driver)
    avtor_page.vizit()
    avtor_page.registr_email_small_pass()
    # Проверяем, что появилась надпись "Длина пароля должна быть не менее 8 символов"
    assert avtor_page.get_snall_pass().is_displayed()


#Регистрация с паролем кирилицей
def test_reg_pass_kir(driver):
    avtor_page = AvtorizashionPage(driver)
    avtor_page.vizit()
    avtor_page.registr_email_pass_kir()
    #Проверяем, что появилась надпись "Пароль должен содержать только латинские буквы"
    assert avtor_page.get_pass_kir().is_displayed()


#Регмстрация с несовпадающими паролями
def test_reg_pass_different(driver):
    avtor_page = AvtorizashionPage(driver)
    avtor_page.vizit()
    avtor_page.registr_pass_different()
    # Проверяем, что появилась надпись "Пароли не совпадают"
    assert avtor_page.get_pass_different().is_displayed()


#Регмстрация с простым паролем
def test_reg_pass_simple(driver):
    avtor_page = AvtorizashionPage(driver)
    avtor_page.vizit()
    avtor_page.registr_pass_simple()
    # Проверяем, что появилась надпись "Пароль ненадежный. Необходимо придумать более сложный пароль."
    assert avtor_page.get_pass_simple().is_displayed()


#Регмстрация с паролем из строчных букв
def test_reg_pass_str(driver):
    avtor_page = AvtorizashionPage(driver)
    avtor_page.vizit()
    avtor_page.registr_pass_str()
    # Проверяем, что появилась надпись ""Пароль должен содержать хотя бы одну заглавную букву"
    assert avtor_page.get_pass_str().is_displayed()

#Регмстрация с паролем без цифр
def test_reg_pass_no_numbers(driver):
    avtor_page = AvtorizashionPage(driver)
    avtor_page.vizit()
    avtor_page.registr_pass_no_numbers()
    # Проверяем, что появилась надпись "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"
    assert avtor_page.get_pass_no_numbers().is_displayed()






