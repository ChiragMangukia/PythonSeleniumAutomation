import time
import MyMethods


driver = MyMethods.invokeChrome()
driver.get("https://www.gmail.com")
driver.find_element_by_id("identifierId").send_keys("adcdefg777")
