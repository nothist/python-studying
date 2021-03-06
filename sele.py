from selenium import webdriver
import time

# options = webdriver.ChromeOptions()
# options.add_argument('-ignore-certificate-errors')
# options.add_argument('-ignore -ssl-errors')
# ,chrome_options=options

chrome_driver = r'C:\Users\V v V\AppData\Local\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get('https://www.jd.com/')
driver.find_element_by_id("key").send_keys("笔记本")
driver.find_element_by_class_name("button").click()
time.sleep(10)
driver.quit()
