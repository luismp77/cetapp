import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime, timedelta
import time
from selenium.common.exceptions import NoSuchElementException


class IncidentePage:
    btn_incidente = (
        By.XPATH, "/html[1]/body[1]/div[1]/aside[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/a[1]/span[2]")
    texto_incidente = (By.XPATH, "//h1[contains(text(),'Incidentes')]")
    btn_nuevo_incidente = (
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/button[1]")
    desplegable_plantilla_datos = (
        By.XPATH, "//body/div[@id='app']/main[@id='mainSection']/div[@id='main-section']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]")
    plantilla_acciones_lm = (
        By.XPATH, "//span[contains(text(),'plantilla con acciones LM')]")
    desplegable_establecimiento = (
        By.XPATH, "//body/div[@id='app']/main[@id='mainSection']/div[@id='main-section']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/*[1]")
    establecimiento_uno = (
        By.XPATH, "/html[1]/body[1]/div[2]/div[1]/ul[1]/li[1]/span[1]")
    desplegable_nueva_area = (
        By.XPATH, "//body/div[@id='app']/main[@id='mainSection']/div[@id='main-section']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/*[1]")
    area_uno = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/ul[1]/li[1]/span[1]")
    desplegable_tipo_incidente = (
        By.XPATH, "//body/div[@id='app']/main[@id='mainSection']/div[@id='main-section']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/*[1]")
    incidente_caida_agua = (
        By.XPATH, "//span[contains(text(),'Caidas de Agua')]")
    btn_fecha_ocurrencia_datos = (
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/span[1]/button[1]")
    flecha_minuto = (
        By.XPATH, "//tbody/tr[3]/td[2]/span[1]")
    seleccion_afuera_fecha = (
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")
    respuesta_flash = (
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
    btn_enviar_investigacion = (
        By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]")
    btn_si_confirmar_investigacion = (
        By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[6]/button[3]")
    btn_aceptar_popup = (
        By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[6]/button[1]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("boton incidente menu lateral")
    def click_incidente(self):
        incidente = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_incidente)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert incidente.is_displayed()
            incidente.click()

    @allure.step("Verificacion Pantalla Incidentes")
    def Titulo(self):
        titulo_real = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.texto_incidente)
        )

        with allure.step("verificar que se muestre el elmento"):

            assert titulo_real.is_displayed()

    @allure.step("Boton nuevo incidente")
    def nuevoIncidente(self):
        Alta = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_nuevo_incidente)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert Alta.is_displayed()
            Alta.click()

    @allure.step("campo plantilla")
    def nuevaPlantilla(self):
        plantilla = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.desplegable_plantilla_datos)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert plantilla.is_displayed()
            plantilla.click()

    @allure.step("seleccion de plantilla")
    def seleccionPlantilla(self):
        plantilla_seleccionada = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.plantilla_acciones_lm)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert plantilla_seleccionada.is_displayed()
            plantilla_seleccionada.click()

    @allure.step("campo establecimiento")
    def nuevaestablecimiento(self):
        establecimiento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.desplegable_establecimiento)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert establecimiento.is_displayed()
            establecimiento.click()

    @allure.step("seleccion establecimiento")
    def seleccionestablecimiento(self):
        establecimiento_seleccionado = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.establecimiento_uno)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert establecimiento_seleccionado.is_displayed()
            establecimiento_seleccionado.click()

    @allure.step("campo area")
    def area(self):
        area = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.desplegable_nueva_area)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert area.is_displayed()
            area.click()

    @allure.step("seleccion area")
    def nuevaArea(self):
        area_nueva = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.area_uno)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert area_nueva.is_displayed()
            area_nueva.click()

    @allure.step("campo Tipo Incidente")
    def tipoIncidente(self):
        tipo_incidente = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.desplegable_tipo_incidente)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert tipo_incidente.is_displayed()
            tipo_incidente.click()

    @allure.step("Seleccion Tipo Incidente")
    def seleccionTipoIncidente(self):
        seleccion_incidente = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.incidente_caida_agua)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert seleccion_incidente.is_displayed()
            seleccion_incidente.click()

    @allure.step("campo Fecha y Hora de Ocurrencia")
    def fecha_Ocurrencia(self):
        fecha_ocurrencia = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_fecha_ocurrencia_datos)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert fecha_ocurrencia.is_displayed()
            fecha_ocurrencia.click()

    @allure.step("campo calendario")
    def colocar_hora(self):
        minutos = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.flecha_minuto)
        )
        with allure.step("verificar que se muestre el elmento"):

            minutos.click()

    @allure.step("seleccion de horario")
    def click_afuera(self):
        seleccion_hora = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.seleccion_afuera_fecha)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert seleccion_hora.is_displayed()
            seleccion_hora.click()

    @allure.step("Estado Reporte flash")
    def responder_repuesta_flash(self):
        respuesta_flash_one = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.respuesta_flash)
        )
        with allure.step("verificar que se muestre el elmento"):
            assert respuesta_flash_one.is_displayed()
            respuesta_flash_one.send_keys("Pruebas Automatizadas")
            sleep(2)

    @allure.step("seleccion boton Enviar a Investigacion")
    def click_enviar_investigacion(self):
        enviar_investigacion = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_enviar_investigacion)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert enviar_investigacion.is_displayed()
            enviar_investigacion.click()

    @allure.step("Confirmacion de envio")
    def click_si_envio(self):
        si_envio = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.btn_si_confirmar_investigacion)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert si_envio.is_displayed()
            si_envio.click()

    @allure.step("Boton Aceptar pop up")
    def click_aceptar_popup(self):
        aceptar_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_aceptar_popup)
        )
        with allure.step("verificar que se muestre el elmento"):

            assert aceptar_popup.is_displayed()
            aceptar_popup.click()
