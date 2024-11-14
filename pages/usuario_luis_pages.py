import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime, timedelta
import time
from selenium.common.exceptions import NoSuchElementException


class usuariPages:
    btn_iniciar1 = (By.XPATH, "//span[contains(text(),'Iniciar sesión')]")
    btn_usuario1 = (By.XPATH, "//input[@id='username']")
    btn_contraseña1 = (By.XPATH, "//input[@type='password']")
    btn_configuracion1 = (
        By.XPATH, "//body/div[@id='app']/aside[@id='sidenav-main']/div[1]/div[1]/div[1]/div[1]/div[9]/div[1]/div[1]/a[1]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Usuarioss")
    def usuario1(self):
        usuarioo1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.btn_usuario1)
        )
        with allure.step("verificar que se muestre el elmento"):
            assert usuarioo1.is_displayed()
            usuarioo1.send_keys("lperez@cetapsa.com")
            sleep(2)

    @allure.step("password")
    def ingresar_contraseña1(self):
        contraseñas1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_contraseña1)
        )
        with allure.step("verificar que se muestre el elmento"):
            assert contraseñas1.is_displayed()
            contraseñas1.send_keys("1234567891")
            sleep(2)

    @allure.step("iniciar")
    def iniciar11(self):
        iniciar1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_iniciar1)
        )
        with allure.step("click en iniciar"):
            iniciar1.is_displayed()
            iniciar1.click()
