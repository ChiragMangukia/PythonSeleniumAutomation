import os
from selenium import webdriver


def invokeChrome():
    return webdriver.Chrome("chromedriver_win32\chromedriver.exe")


def invokeFirefox():
    return webdriver.Firefox("chromedriver_win32\geckodriver.exe")


def killProcess():
    os.system("taskkill /f /im chromedriver.exe")
