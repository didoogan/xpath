import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#  https://www.google.com.ua/search?q=super+information&biw=1366&bih=673&ei=JM7eV6qoKIaqsQGqrayQBg&start=10&sa=N

driver = webdriver.Firefox()
driver.get(" https://www.google.com.ua/search?q=super+information&biw=1366&bih=673&ei=JM7eV6qoKIaqsQGqrayQBg&start=10&sa=N")
# elem = driver.find_element_by_name("q")
# elem.send_keys("super information")
# elem.send_keys(Keys.RETURN)




# try:
#     second_page = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Page 2']"))

#     )
# except:
#     print 'errot'
# print 'SECOND PAGE: ', second_page.get_attribute('href')
# driver.get(second_page.get_attribute('href'))

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


# import pdb; pdb.set_trace()


def get_data(items):
	with open('data2.csv','a') as csvfile:
		fieldnames = ['index', 'head', 'url']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		for index, value  in enumerate(items):
			import pdb; pdb.set_trace()
			a =  value.find_element_by_xpath("div/h3/a")
			url = value.find_element_by_xpath("div/div/div/div/cite")
			writer.writerow({'index': index, 'head': a.text.encode('utf-8'), 'url': url.text.encode('utf-8') })

	

get_data(divs)
# import pdb; pdb.set_trace()
# url = second_page.get_attribute('href')	

# driver.get(url)

# try:
#     divs2 = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located((By.XPATH, "//div[@class='g']"))

#     )
# except:
#     print 'errot'
# import pdb; pdb.set_trace()    
# get_data(divs2)

# driver.quit()
