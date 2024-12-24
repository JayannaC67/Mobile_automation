import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from appium.webdriver.appium_service import AppiumService
from appium.options.common import AppiumOptions
import time
import json


@pytest.fixture()
def appiumDriverWEB(request):
    appium_service = AppiumService()
    try:
        # to start Appium server
        appium_service.start(args=['--base-path', '/wd/hub'])
        time.sleep(10)
        print("Appium Server started")
        print("Launch The Chrome Browser")

        # Define Capabilities:
        desired_caps = {
            "deviceName": "Samsung",
            "platformName": "Android",
            "version": "9.0",
            "automationName": "UiAutomator2",
            "udid": "emulator-5554",
            "browserName": "chrome",
            "chromedriverExecutable": "C:\\Users\LenT14G2ITL\Downloads\chromedriver-win64\chromedriver-win64\\chromedriver.exe"
        }

        # Initialization of Webdriver with URL and capabilities
        driver = webdriver.Remote("http://localhost:4723/wd/hub",
                                  options=AppiumOptions().load_capabilities(desired_caps))

        # This is instance level webdriver initialization before and after browser instance will create and close
        request.instance.driver = driver

        yield driver
        driver.quit()
        print("Quit web driver session")

        # To stop the appium service
        appium_service.stop()
        print("Appium server is stopped")

    except TypeError:
        print("Appium server is having some issue")
        appium_service.stop()
        print("Appium server is stopped")


# This is for reading data from json file
@pytest.fixture()
def readJson():
    with open('Test Data\global.json') as json_file:
        data = json.load(json_file)
        return data