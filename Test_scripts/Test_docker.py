import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
import time
#from Page_Object_Model.Launch_page_object import SJOrangeHRM
import time
from appium.webdriver.common.appiumby import AppiumBy


class TestDockerInMobileChrome:

    def test_ui_Docker(self, appiumDriverWEB):
        appiumDriverWEB.get("https://www.docker.com/")
        appiumDriverWEB.update_settings({"waitForIdleTimeout": 1000})
        time.sleep(5)
        appiumDriverWEB.find_element(AppiumBy.XPATH, "//li[@class='mobile-toggle']").is_displayed()
        print("The Hamberg menu option is available ..... as expected ...")



'''
1. Download Python and install it and do class path set.
2. Download an install Android Studio and set Android_Home In enviornment set variable add path        <C:\\Users\Qualitrix\AppData\Local\Android\Sdk\platform-tools>

3. Install npm
4. Verify npm version by entering "npm" in cmd
5. Create cloud device using Android studio or connect physical device with developer mode enable (inside Developer setting enable "USB Debugging"  and "disable permission monitoring")
6. Open cmd and type "adb devices" -> should return device UDID
7. Copy the same UDID in your code (capabilities sections) [This is required, if multiple devices are connected, else not required]
8. In cmd, 
    Enter "pip install appium -python -client"  -> To install python appium client
    Enter "appium driver install uiautomator2"  -> To Install UIAutomator2
9. Start Appium server using cmd, enter "appium --base-path /wd/hub"  [This is manually to start the appium server, this step can be skip through code]
10. Check your device chrome browser version and download the same version chrome driver executable file. 
11. Need to create a capability object which should have the platform version, platform number, platform type, udid, device name, browser name and chrome driver executable path.
'''