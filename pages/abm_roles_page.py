import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime, timedelta
import time
from selenium.common.exceptions import NoSuchElementException


class AbmPage:
    """
    locator y acciones de los Abms que esta en el modulo de configuración.
    """

    btn_generales = (
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/span[1]")
    roles = (
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/a[1]/div[1]/span[1]")
    btn_nuevo_rol = (
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/button[1]")
    empresa = (
        By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]")
    empresa_c = (
        By.XPATH, "/html[1]/body[1]/div[3]/div[2]/ul[1]/li[5]/span[1]")
    descripcion = (
        By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]")
    btn_enviar = (
        By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/div[1]/div[1]/button[1]")
    btn_aceptar = (By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[6]/button[1]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("generales3")
    def generales1(self):
        jefe = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_generales)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert jefe.is_displayed()
            jefe.click()

    @allure.step("rolesss")
    def click_rol(self):
        roless = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.roles))

        with allure.step("verificar elemento roles"):
            assert roless.is_displayed()
            roless.click()

    @allure.step("verificar boton + rol")
    def click_nuevo_rol(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_nuevo_rol)
        )
        with allure.step("hacemos click"):
            self.driver.find_element(
                *self.btn_nuevo_rol).click()
            sleep(3)

    @allure.step("hacemos click en empresa y verificamos")
    def click_empresa_rol(self):
        clickk = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.empresa)
        )
        with allure.step("hacemos click"):
            assert clickk.is_displayed()
            clickk.click()
        sleep(3)

    @allure.step("seleccionar empresa")
    def seleccion_empresa_rol(self):
        empresa_cc = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.empresa_c)
        )
        with allure.step("seleccionar empresa"):
            assert empresa_cc.is_displayed()
            empresa_cc.click()
        sleep(3)

    @allure.step("ingresar descripcion")
    def ingresar_descripcion(self):
        descripciones = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.descripcion)
        )
        with allure.step("seleccionar empresa"):
            assert descripciones.is_displayed()
            descripciones.click()
            descripciones.send_keys("pruebas automatizadas")
        sleep(3)

    @allure.step("enviar")
    def ingresar_enviar(self):
        enviamos = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_enviar)
        )
        with allure.step("seleccionar enviar"):
            assert enviamos.is_displayed()
            enviamos.click()
            sleep(7)

    @allure.step("enviar aceptar")
    def ingresar_aceptar(self):
        acerta = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_aceptar)
        )
        with allure.step("seleccionar aceptar"):
            assert acerta.is_displayed()
            acerta.click()
            sleep(7)
