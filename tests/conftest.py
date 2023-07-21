import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach
from utils.base_session import BaseSession

load_dotenv()
authorization_cookie = None


@pytest.fixture(scope='session')
def demoshop():
    return BaseSession(os.getenv("API_URL"))


@pytest.fixture(scope='function')
def app(demoshop):
    global authorization_cookie
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN_SELENOID')
    password = os.getenv('PASSWORD_SELENOID')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver
    browser.config.base_url = (os.getenv("API_URL"))
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    if authorization_cookie is None:
        response = demoshop.post(
            "login", json={"Email": os.getenv("LOGIN"), "Password": os.getenv("PASSWORD")}, allow_redirects=False)
        authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.open("Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    yield browser
    attach.add_screenshot(browser)
    attach.add_video(browser)


@pytest.fixture(scope='session')
def reqres():
    return BaseSession(os.getenv("REQ_URL"))




