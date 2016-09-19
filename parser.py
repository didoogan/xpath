import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("http://www.google.com")

def get_query(query):
    elem = driver.find_element_by_name("q")
    elem.send_keys(query)
    elem.send_keys(Keys.RETURN)



def get_divs():
    try:
        divs = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='g' and not(@id)]"))
        )
        return divs
    except:
        print 'errot'


def get_page(number):
    try:
        # import pdb; pdb.set_trace()
        page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@aria-label="Page {}"]'.format(number)))
            # EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Page 2']"))
        )
        url = page.get_attribute('href')
        driver.get(url)
        # return page
    except:
        print 'get_page error'


def get_data(items):
	with open('data.csv','a') as csvfile:
		fieldnames = ['index', 'head', 'url']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		for index, value  in enumerate(items):
			a =  value.find_element_by_xpath("div/h3/a")
			url = value.find_element_by_xpath("div/div/div/div/cite")
			writer.writerow({'index': index, 'head': a.text.encode('utf-8'), 'url': url.text.encode('utf-8') })

def get_result(number):
    divs = get_divs()
    get_data(divs)
    for i in range(2,number+1):
        get_page(i)
        divs = get_divs()
        get_data(divs)

get_query("information")
get_result(5)
driver.close()


	
