import MyMethods
import time

driver = MyMethods.invokeChrome()
driver.get("http://www.google.com")
print(driver.title)
driver.find_element_by_id("lst-ib").send_keys("Hello World!")
time.sleep(5)
driver.quit()