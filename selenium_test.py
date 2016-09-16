from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("some text")
elem.send_keys(Keys.RETURN)


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='g'][1]/div/h3/a"))

    )
    # import pdb; pdb.set_trace()
    element = element.get_attribute('text')
finally:
    driver.quit()

print element
