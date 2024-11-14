import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime, timedelta
import time
from selenium.common.exceptions import NoSuchElementException


class CetappPage:
    btn_iniciar = (By.XPATH, "//span[contains(text(),'Iniciar sesión')]")
    btn_usuario = (By.XPATH, "//input[@id='username']")
    btn_contraseña = (By.XPATH, "//input[@type='password']")
    btn_configuracion = (
        By.XPATH, "//body/div[@id='app']/aside[@id='sidenav-main']/div[1]/div[1]/div[1]/div[1]/div[9]/div[1]/div[1]/a[1]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Usuario")
    def usuario(self):
        usuarioo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.btn_usuario)
        )
        with allure.step("verificar que se muestre el elmento"):
            assert usuarioo.is_displayed()
            usuarioo.send_keys("superusuario")
            sleep(2)

    @allure.step("password")
    def ingresar_contraseña(self):
        contraseñas = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_contraseña)
        )
        with allure.step("verificar que se muestre el elmento"):
            assert contraseñas.is_displayed()
            contraseñas.send_keys("Cetap!2017")
            sleep(2)

    @allure.step("iniciar")
    def iniciar(self):
        clickIniciar = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_iniciar)
        )
        with allure.step("click en iniciar"):
            clickIniciar.click()

    @allure.step("configuracion")
    def click_configuracion(self):
        jefe1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_configuracion)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert jefe1.is_displayed()
            jefe1.click()
