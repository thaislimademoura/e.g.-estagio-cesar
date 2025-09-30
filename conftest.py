# conftest.py
import pytest
from selenium import webdriver
import json
from pathlib import Path
import time
import os, pytest_html
import csv
report_data = []
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)")
# pra rodar o mesmo teste em diferentes browsers
# @pytest.fixture
@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    # browser = request.config.getoption("--browser").lower()
    browser = request.param
    if browser == "chrome":
        driver_instance = webdriver.Chrome()
    elif browser == "firefox":
        driver_instance = webdriver.Firefox()
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")
    driver_instance.maximize_window()
    request.node.browser = browser
    yield driver_instance
    driver_instance.quit()
# vai gerar na raiz do projeto um test duration
LOG_FILE = Path("test_durations.log")
#apaaga test data, o tool tips q tava chamando ele vai falhar
# @pytest.fixture #notacao do pytest
# def test_data(): #feature para carregar o json
#     with open("data/test_data.json") as f:
#         return json.load(f)
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
    """Mostra o tempo de duracao do teste e salva e arquivo html"""
    duration = time.time() - item.start_time
    msg = f"[END] Test '{item.nodeid}' finished in {duration:.2f} seconds."
    print(msg)
    # salva em arquivo
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")
#docstype tem que ser dentro da funcao
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """ Funcao para tirar print do erro e botar no html"""
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" and report.failed:
        # Create screenshots directory if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        # Take screenshot
        driver = item.funcargs['driver']
        screenshot_file = os.path.join("screenshots", f"{item.name}_error.png")
        driver.save_screenshot(screenshot_file)
        # Add screenshot to the HTML report
        if screenshot_file:
            html = f'<div><img src="{screenshot_file}" alt="screenshot" style="width:304px;height:228px;" ' \
           f'onclick="window.open(this.src)" align="right"/></div>'
            extra.append(pytest_html.extras.html(html))
    report.extra = extra
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call": # and report.failed:
        status = 'Passed' if report.passed else 'Failed'
        browser = getattr(item, 'browser', 'N/A')
        test_name = item.name
        duration = f"{report.duration:.4f}s"
        if report.failed:
            # Create screenshots directory if it doesn't exist
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            # Take screenshot
            driver = item.funcargs['driver']
            screenshot_file = os.path.join("screenshots", f"{item.name}_error.png")
            driver.save_screenshot(screenshot_file)
            # Add screenshot to the HTML report
            if screenshot_file:
                html = f'<div><img src="{screenshot_file}" alt="screenshot" style="width:304px;height:228px;" ' \
            f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report_data.append({
            "browser": browser.capitalize(),
            "test_case_name": test_name,
            "status": status,
            "timestamp": duration
        })
    report.extra = extra
def pytest_sessionfinish(session):
    """
    Hook executed in the end of test session to create the CSV report.
    """
    if not report_data:
        return
    # Ordena os dados por navegador para um relatório mais legível
    sorted_reports = sorted(report_data, key=lambda x: x['browser'])
    keys = sorted_reports[0].keys()
    with open('test_report.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(sorted_reports)
    print("\nReport 'test_report.csv' generated successfully")

@pytest.fixture(scope="class")
def class_resource():
    print("\n[SETUP] class_resource")
    yield "class fixture"
    print("[TEARDOWN] class_resource")

@pytest.fixture(scope="module")
def module_resource():
    print("\n[SETUP] module_resource")
    yield "module fixture"
    print("[TEARDOWN] module_resource")

@pytest.fixture(scope="session")
def session_resource():
    print("\n[SETUP] session_resource")
    yield "session fixture"
    print("[TEARDOWN] session_resource")