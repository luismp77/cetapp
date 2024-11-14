import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.abm_roles_page import AbmPage
from time import sleep
from config.browser import BrowserConfig
from pages.incidente_pages import IncidentePage
from pages.usuario_luis_pages import usuariPages


class Testa:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://cetappgowebtest.z20.web.core.windows.net/")
        yield  # Lo que este despues de yield se ejecuta despues de cada test
        print("Cerrar Browser")
        self.driver.quit()

    @allure.title("Validar ABM rol base")
    @allure.description("Validar configuracion de rol base")
    def test_rol_base(self):

        with allure.step("nos dirigimos a configuraciones"):
            driver = self.driver
            sleep(3)
            usuario_pages = usuariPages(driver)
            incidentes_pagess = IncidentePage(driver)
            usuario_pages.usuario1()
            usuario_pages.ingresar_contraseña1()
            usuario_pages.iniciar11()
            sleep(3)
            incidentes_pagess.click_incidente()
            incidentes_pagess.Titulo()
            sleep(3)
            incidentes_pagess.nuevoIncidente()
            incidentes_pagess.nuevaPlantilla()
            sleep(2)
            incidentes_pagess.seleccionPlantilla()
            sleep(2)
            incidentes_pagess.nuevaestablecimiento()
            sleep(2)
            incidentes_pagess.seleccionestablecimiento()
            sleep(3)
            incidentes_pagess.area()
            incidentes_pagess.nuevaArea()
            incidentes_pagess.tipoIncidente()
            incidentes_pagess.seleccionTipoIncidente()
            incidentes_pagess.fecha_Ocurrencia()
            sleep(2)
            incidentes_pagess.colocar_hora()
            sleep(2)
            incidentes_pagess.click_afuera()
            sleep(2)
            incidentes_pagess.responder_repuesta_flash()
            incidentes_pagess.click_enviar_investigacion()
            incidentes_pagess.click_si_envio()
            incidentes_pagess.click_aceptar_popup()
            sleep(4)

            # abm_pages.ingresar_env
            # iar()
            # sleep(3)
            # abm_pages.ingresar_enviar()
            # sleep(3)


if __name__ == "__main__":
    pytest.main()
