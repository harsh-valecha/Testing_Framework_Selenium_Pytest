# Automation Framework

This automation framework is built using `pytest` and `Selenium WebDriver` to provide a robust and flexible testing environment. It supports multiple features that enhance test automation capabilities, including detailed reporting, logging, and data-driven testing.

## Key Features

1. **HTML Reports**: Automatically generates comprehensive HTML reports after each test run, providing detailed information on test execution status, including passed, failed, and skipped tests.

2. **Logging**: Saves detailed logs of test execution, which are helpful for debugging and understanding the flow of the tests. Logs include information such as test start and end times, steps executed, and error messages if any.

3. **Screenshots on Test Failure**: Captures screenshots automatically when a test fails, making it easier to diagnose issues by visually inspecting the state of the application at the time of failure.

4. **Data-Driven Testing**: Supports data-driven testing using various data sources like CSV files, JSON files, and SQL databases. This allows tests to be run with multiple sets of input data to ensure comprehensive coverage.

5. **Page Object Model (POM)**: Implements the Page Object Model design pattern to enhance test maintenance and readability. This approach separates test logic from page structure, making tests easier to manage and less prone to breaking when the UI changes.

## Installation

To use this framework, ensure you have Python installed on your system. Then, install the required dependencies:

```bash
pip install -r requirements.txt
