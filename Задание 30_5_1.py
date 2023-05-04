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
        #Открыть  страницу входа на сайт PetFriend b ввести логин и пороль
        self.driver.find_element(By.XPATH,'//input[@id="email"]').send_keys(self.user)
        self.driver.find_element(By.XPATH,'//input[@id="pass"]').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//button[@class="btn btn-success"][text()="Войти"]').click()
        sleep(5)
        #assert WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME,("h1").text)))=="PetFriends"
        #assert WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//h1[@class="text-center"][text()="PetFriends"]')))
        # На гланой странице нажать кнопку "меню"
        self.driver.find_element(By.CLASS_NAME, "navbar-toggler-icon").click()
        #В открывшемся окне нажать кнопку "мои птомцы"
        self.driver.find_element(By.XPATH,'//a[@class="nav-link"][text()="Мои питомцы"]').click()


    def test_count(self):       # Проверка числинности ритомцев (согласно статмке)
        self.open()
        self.login()
        self.driver.implicitly_wait(10)
        assert len(self.driver.find_elements(By.XPATH,'//th/img[@src]'))==8
        self.close()


    def test_photo(self):       #Проверка, что фото имеют больше половины питомцев
        self.open()
        self.login()
        # Определяем число питомцев
        count_all=len(WebDriverWait(self.driver, 10).until\
            (EC.presence_of_all_elements_located((By.XPATH, '//th/img[@src]'))))
        #Число питомцев без фото
        count_no_photo=len(WebDriverWait(self.driver, 10).until\
            (EC.presence_of_all_elements_located((By.XPATH, '//th/img[@src=""]'))))
        assert (count_all-count_no_photo) > count_all/2
        self.close()


    #Проверка, что у всех питомцев есть имя, возраст и порода.
    #В каждой картрчке есть тексты имя, возраст,  порода и кнопка с всплывающим текстом "удалить питомца"
    #Если будет 8*4=32 значения, значит у всех питомцев есть имя, возраст и порода

    def test_name_age_breed(self):
        self.open()
        self.login()
        assert len(WebDriverWait(self.driver, 10).until\
                  (EC.presence_of_all_elements_located((By.XPATH,'//td[text()]'))))==32
        self.close()

    #Проверка, что все имена разные
    def test_different_names(self):
        self.open()
        self.login()
     #Находим вебэлементы всех питомцев
        web = WebDriverWait(self.driver, 10).until \
         (EC.presence_of_all_elements_located((By.XPATH, '//td[text()]')))
     #Преобразуем в массив карточек питомцев (имя, порода, возраст)
        card=[]
        for job in web:
           card.append(job.text)

     #Оставляем массив имён
        name=[card[0],card[4],card[8],card[12],card[16],card[20],card[24],card[28]]
     #Массив имён из статики
        name_st=['Баюн','чебурашка','Шар','Сигма','Василий','попка','Жердяй','Чита']

        assert set(name_st)==set(name)
        self.close()


