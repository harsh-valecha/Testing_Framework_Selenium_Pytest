from selenium import webdriver
from utils.config import Config

def get_driver():
    if Config.BROWSER == 'chrome':
        return webdriver.Chrome()
    elif Config.BROWSER == 'firefox':
        return webdriver.Firefox()
    else:
        raise Exception(f"Browser {Config.BROWSER} is not supported.")
