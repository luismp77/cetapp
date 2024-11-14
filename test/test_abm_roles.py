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
from pages.home_page import CetappPage


class Test:

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
            home_pages = CetappPage(driver)
            abm_pages = AbmPage(driver)
            home_pages.usuario()
            home_pages.ingresar_contraseña()
            home_pages.iniciar()
            sleep(3)
            home_pages.click_configuracion()
            abm_pages.generales1()
            sleep(3)
            abm_pages.click_rol()
            abm_pages.click_nuevo_rol()
            sleep(2)
            abm_pages.click_empresa_rol()
            sleep(2)
            abm_pages.seleccion_empresa_rol()
            sleep(2)
            abm_pages.ingresar_descripcion()
            sleep(3)
            # abm_pages.ingresar_enviar()
            # sleep(3)
            # abm_pages.ingresar_enviar()
            # sleep(3)


if __name__ == "__main__":
    pytest.main()
