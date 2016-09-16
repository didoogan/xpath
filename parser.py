import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("http://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("super information")
elem.send_keys(Keys.RETURN)

row = []


try:
    divs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='g']"))

    )
except:
    print 'errot'


# def get_data(list):
# 	with open('data.csv','a') as f1:
#     	writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
# 	for index, value  in enumerate(list):
# 		print index
# 		print 'index :', index
# 		a =  value.find_element_by_xpath("div/h3/a")
# 		print 'head :', a.text
# 		url = value.find_element_by_xpath("div/div/div/div/cite")
# 		print 'url :', url.text
# 		# import pdb; pdb.set_trace()
# 	second_page = value.find_element_by_xpath("//a[@aria-label='Page 2']")
# 	return second_page.get_attribute('href')

try:
    second_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Page 2']"))

    )
except:
    print 'errot'


def get_data(items):
	with open('data.csv','a') as csvfile:
		fieldnames = ['index', 'head', 'url']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		for index, value  in enumerate(items):
			a =  value.find_element_by_xpath("div/h3/a")
			url = value.find_element_by_xpath("div/div/div/div/cite")
			writer.writerow({'index': index, 'head': a.text.encode('utf-8'), 'url': url.text.encode('utf-8') })

	

get_data(divs)
# import pdb; pdb.set_trace()
url = second_page.get_attribute('href')	

driver.get(url)

try:
    divs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='g']"))

    )
except:
    print 'errot'
import pdb; pdb.set_trace()    
# get_data(divs)

# driver.quit()
