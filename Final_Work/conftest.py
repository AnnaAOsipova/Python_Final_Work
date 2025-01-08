import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import subprocess

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)

selected_browser = data.get("browser", "chrome")
send_email = str(data.get("send_email", "false")).lower() == "true"

@pytest.fixture(scope="session")
def browser():
    if selected_browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session", autouse=True)
def send_email_after_tests(request):
    if send_email:
        def send():
            try:
                subprocess.run(["python", "mail.py", "report.xml"], check=True)
            except subprocess.CalledProcessError as error:
                print(f"Ошибка при отправке email: {error}")
        request.addfinalizer(send)