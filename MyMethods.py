from selenium import webdriver


def invokeChrome():
    return webdriver.Chrome("BrowserDrivers\chromedriver.exe")


def invokeFirefox():
    return webdriver.Firefox("BrowserDrivers\geckodriver.exe")
