import time
import logging
import MyMethods

FIREFOX = MyMethods.invokeFirefox()

log_filename = 'D:/logger.log'
logging.basicConfig(filename=log_filename, level=logging.DEBUG)

driver = MyMethods.invokeFirefox()
logging.debug('Chrome browser invoked Broswer Version' + driver.capabilities['version'])
driver.get("https://www.gmail.com")
logging.debug('Gmail opened')
driver.find_element_by_id("identifierId").send_keys("adcdefg777")
logging.debug('Entered Email Id')
time.sleep(4)
logging.debug('Slept for 4 seconds')
driver.quit()

MyMethods.killProcess()