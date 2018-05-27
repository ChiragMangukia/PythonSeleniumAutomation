import time
import os
import MyMethods

driver = MyMethods.invokeChrome()
driver.get("https://www.facebook.com")
driver.find_element_by_id("email").send_keys("adcdefg777@gmail.com")
driver.find_element_by_id("pass").send_keys("lovely@06")
driver.find_element_by_xpath("//input[@value='Log In']").click()
driver.quit()
MyMethods.killProcess()
