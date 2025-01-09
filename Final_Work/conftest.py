import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


with open("testdata.yaml") as f:
    data = yaml.safe_load(f)

selected_browser = data.get("browser", "chrome")
send_email = str(data.get("send_email", "false")).lower() == "true"

@pytest.fixture(scope="session")
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
