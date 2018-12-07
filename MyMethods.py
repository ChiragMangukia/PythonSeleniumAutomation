from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def invokeChrome():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    return webdriver.Chrome("BrowserDrivers/chromedriver.exe", chrome_options=chrome_options)

def invokeFirefox():
    return webdriver.Firefox("BrowserDrivers\geckodriver.exe")
