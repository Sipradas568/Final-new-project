import pytest
import yaml
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.microsoft import EdgeChromiumDriverManager




def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "chrome")


@pytest.fixture (scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def driver(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "Edge":
        driver = webdriver.Edge()
    
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def config():
    with open ("Config/config.yaml") as file:
        return yaml.safe_load(file)

    
@pytest.fixture
def base_url(config):
    return config.get("base_url")
