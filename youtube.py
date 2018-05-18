from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:/Users/hanta/Desktop/Spyder/chromedriver/chromedriver.exe')
#driver.get("http://www.python.org")
driver.get("https://www.youtube.com/")
#assert "Python" in driver.title
elem = driver.find_element_by_tag_name("input")
elem.clear()
elem.send_keys("Python")
elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
