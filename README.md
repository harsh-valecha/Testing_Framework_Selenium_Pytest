## Automation Framework for testing using selenium and pytest 

### Project Structure
```
.
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── conftest.py
├── pages/
│   ├── __init__.py
│   ├── login_page.py
├── utils/
│   ├── __init__.py
│   ├── config.py
│   ├── driver_factory.py
├── reports/
│   ├── report.html
├── screenshots/
├── requirements.txt
├── pytest.ini
```

### requirements.txt
This file lists all the dependencies required for the project. 

```plaintext
selenium
pytest
pytest-html
```

- **selenium**: Used for browser automation.
- **pytest**: The testing framework.
- **pytest-html**: A plugin for pytest that generates HTML reports.

### pytest.ini
This configuration file is used to customize pytest behavior.

```ini
[pytest]
addopts = --html=reports/report.html --self-contained-html
```

- `addopts`: Command line options to be added by default. Here, it generates an HTML report at `reports/report.html`.

### conftest.py
This file contains fixtures that are shared across multiple test files.

```python
import pytest
from selenium import webdriver
from utils.driver_factory import get_driver

@pytest.fixture(scope='session')
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
```

- **driver()**: A fixture that sets up the Selenium WebDriver and tears it down after the test session is completed. The scope is set to 'session' to reuse the browser instance across all tests.

### utils/config.py
This file contains configuration settings used throughout the framework.

```python
class Config:
    BASE_URL = 'http://example.com'
    BROWSER = 'chrome'
```

- **Config**: A class holding configuration values such as the base URL of the application and the browser to be used.

### utils/driver_factory.py
This file handles the creation of browser drivers.

```python
from selenium import webdriver
from utils.config import Config

def get_driver():
    if Config.BROWSER == 'chrome':
        return webdriver.Chrome()
    elif Config.BROWSER == 'firefox':
        return webdriver.Firefox()
    else:
        raise Exception(f"Browser {Config.BROWSER} is not supported.")
```

- **get_driver()**: A function that returns a WebDriver instance based on the browser specified in the Config class.

### pages/login_page.py
This file follows the Page Object Model (POM) pattern and encapsulates the login page functionality.

```python
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login')

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
```

- **LoginPage**: A class representing the login page.
    - **__init__(self, driver)**: Initializes the page with the WebDriver instance.
    - **enter_username(self, username)**: Enters the username in the username field.
    - **enter_password(self, password)**: Enters the password in the password field.
    - **click_login(self)**: Clicks the login button.

### tests/test_login.py
This file contains test cases for the login functionality.

```python
import pytest
from utils.config import Config
from pages.login_page import LoginPage

def test_login(driver):
    driver.get(Config.BASE_URL)
    
    login_page = LoginPage(driver)
    login_page.enter_username('testuser')
    login_page.enter_password('password')
    login_page.click_login()

    assert "Dashboard" in driver.title
```

- **test_login(driver)**: A test function that performs the login test.
    - **driver.get(Config.BASE_URL)**: Navigates to the base URL of the application.
    - **LoginPage(driver)**: Initializes the login page object.
    - **enter_username('testuser')**: Enters the username.
    - **enter_password('password')**: Enters the password.
    - **click_login()**: Clicks the login button.
    - **assert "Dashboard" in driver.title**: Asserts that the title of the page contains "Dashboard" to verify a successful login.

### `__init__.py`
Empty `__init__.py` files are used to mark directories as Python packages. These can be empty or contain initialization code for the package.

### reports/report.html
This is the output HTML report generated by pytest-html. It contains the results of the test execution in an easy-to-read format.

### Running the Tests
To run the tests and generate an HTML report, use the following command:
```bash
pytest
```

This command will execute all the tests in the `tests` directory and generate an HTML report at `reports/report.html`.

By following this structure, you have a modular, maintainable, and scalable test automation framework. You can extend it by adding more page objects, utilities, and test cases as needed.
