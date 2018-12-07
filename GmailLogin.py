import time
import logging
import MyMethods


log_filename = 'D:/logger.log'
logging.basicConfig(filename=log_filename, level=logging.DEBUG)

driver = MyMethods.invokeChrome()
logging.debug('Chrome browser invoked')
logging.debug('Browser Version ' + driver.capabilities['version'])

try:
    driver.get("https://accounts.google.com")
    logging.debug('Gmail opened')
    driver.find_element_by_id("identifierId").send_keys("adcdefg777")
    logging.debug('Entered Email Id')
    time.sleep(3)
    logging.debug('Slept for 3 seconds')
    driver.quit()

    MyMethods.killProcess()

except Exception as e:
    logging.debug(e)
