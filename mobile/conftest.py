import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
import json
from pathlib import Path

@pytest.fixture(scope="function")
def driver():
    # --- SETUP PHASE ---
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.saucelabs.mydemoapp.android",
        "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
    }) 
    _driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
    # The 'yield' keyword passes control to the test function
    yield _driver
    
    # --- TEARDOWN PHASE ---
    # This code runs AFTER the test function completes (or fails)
    print("\nQuitting driver...")
    _driver.quit()


@pytest.fixture(scope="session")
def load_data_capabilities():
    """Lê o JSON de capabilities e retorna como dicionário"""
    json_path = Path(__file__).parent / "data" / "data_test_mydemoapp_1.json"
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def test_android_capabilities(mobile_capabilities):
    android_caps = mobile_capabilities["android"]
    assert android_caps["platformName"] == "Android"
    assert "deviceName" in android_caps


def test_ios_capabilities(mobile_capabilities):
    ios_caps = mobile_capabilities["ios"]
    assert ios_caps["automationName"] == "XCUITest"