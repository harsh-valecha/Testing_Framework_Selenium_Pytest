import pytest
from selenium import webdriver
from utils.driver_factory import get_driver
import os
import pytest_html

@pytest.fixture(scope='session')
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # We only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        # Get the driver from the fixture
        driver = item.funcargs['driver']
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)  # Ensure the directory exists
        screenshot_file = os.path.join(screenshot_dir, f"{item.name}.png")
        driver.save_screenshot(screenshot_file)

        # Attach the screenshot to the HTML report
        if hasattr(rep, "extra"):
            rep.extra.append(pytest_html.extras.png(screenshot_file))
        else:
            rep.extra = [pytest_html.extras.png(screenshot_file)]