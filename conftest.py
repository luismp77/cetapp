# conftest.py
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from config.browser import BrowserConfig
import os


def pytest_addoption(parser):
    """
    Agregar opciones de línea de comandos para seleccionar el navegador
    """
    parser.addoption("--browser", action="store", default="chrome",
                     help="Escoger navegador: chrome o edge")
    parser.addoption("--ambiente", action="store", default="qa",
                     help="Escoger el ambiente de ejecución: qa o prod")
    # V.NARANJO
    parser.addoption("--nombrearchivo", action="store", default="datos",
                     help="Seleccionar archivo datos:")


def pytest_configure(config):
    os.environ["ambiente"] = config.getoption("ambiente")
    os.environ["browser"] = config.getoption("browser")
    # V.NARANJO
    os.environ["nombrearchivo"] = config.getoption("nombrearchivo")


@pytest.fixture(autouse=True)
def driver(request):
    """
    Fixture para inicializar el driver del navegador
    """
    driver = BrowserConfig(os.getenv("browser")).select_browser()
    driver.maximize_window()
    # V.NARANJO: miximize puede ser reemplazado por seteo en clase ChromiumOptions de options.py -->Método __init__
    # de la carpeta \autoTest\Lib\site-packages\selenium\webdriver\chromium\options.py
    # (self.add_argument("start-maximized"))
    yield driver  # Retorna el objeto driver para que esté disponible en las pruebas

    print("Cerrar Browser")
    driver.quit()
