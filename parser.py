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



try:
    divs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='g']"))

    )
except:
    print 'errot'



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

	
# import pdb; pdb.set_trace()

get_data(divs)
url = second_page.get_attribute('href') 

driver.get(url)

try:
    divs2 = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='g']"))

    )
except:
    print 'errot'
# import pdb; pdb.set_trace()    
# with open('data.csv','a') as csvfile:
#     fieldnames = ['index', 'head', 'url']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     for index, value  in enumerate(divs2):
#         import pdb; pdb.set_trace()    
#         a =  value.find_element_by_xpath("div/h3/a")
#         url = value.find_element_by_xpath("div/div/div/div/cite")
        # writer.writerow({'index': index, 'head': a.text.encode('utf-8'), 'url': url.text.encode('utf-8') })

with open('data.csv','a') as csvfile:
    fieldnames = ['index', 'head', 'url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for i in range(1,10):
        import pdb; pdb.set_trace()    
        # a =  driver.find_element_by_xpath("//div[@class='g'][i]/div/h3/a")
        # url = driver.find_element_by_xpath("//div[@class='g'][i]/div/div/div/div/cite")
        writer.writerow({'index': i, 
            'head': driver.find_element_by_xpath("//div[@class='g'][i]/div/h3/a").encode('utf-8'), 
            'url': driver.find_element_by_xpath("//div[@class='g'][i]/div/div/div/div/cite").encode('utf-8') })
# driver.quit()
