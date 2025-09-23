import pytest
from selenium import webdriver
import json
import time
from pathlib import Path

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()
    if browser == "chrome":
        driver_instance = webdriver.Chrome()
    elif browser == "firefox":
        driver_instance = webdriver.Firefox()
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")
    
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


@pytest.fixture(scope="session")
def test_data():
    with open("data/test_data.json") as f:
        return json.load(f)
    
    
LOG_FILE = Path("test_durations.log")
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    item.start_time = time.time()
    item.start_str = time.strftime("%H:%M:%S", time.localtime())
    msg = f"\n[START] Test '{item.nodeid}' - {item.start_str}"
    print(msg)
    
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")

@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item):
    duration = time.time() - item.start_time
    msg = f"[END] Test '{item.nodeid}' finished in {duration:.2f} seconds."
    print(msg)

    # salva em arquivo
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")