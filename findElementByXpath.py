"""finding element  using Xpath locator
1. import time  from python
2. import webdriver from selenium.
3.import chromedrivermanager.in order to import chromedrivermanager 
ask pip to installwebdriver_manager
4.install chromedrivermanager and assign it to the variale driver.
5.use get fumction to open the web page with the help of url.
ie.driver.get("url")
6.Go to the textbox and right click >> Inspect.
7.On inspecting the web element, it will show an input tag and attributes like class and id.

8.Use the id and these attributes to construct XPath which, in turn, will locate the first name field.
9.similarly for user name 
Go to the username tab and right click >> Inspect.
On inspecting the web element, it will show an input tag and attributes like class and id.
Use the id and these attributes to construct XPath which, in turn, will locate the first name field.
"""
import time#this is python time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager#if weddriver_manager is not found run
#pip install webdrive_manager
driver=webdriver.Chrome(ChromeDriverManager().install())# your entire selenium chrome package
from selenium.webdriver.common.by import By
driver.get("http://omayo.blogspot.com")
time.sleep(3)#this will hold the time for 3 seconds
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//textarea[@rows='10']").send_keys("i want to write something")
time.sleep(5)
driver.find_element(By.XPATH,"//textarea[@cols='30']").send_keys("and its still there")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("amrit_kh3")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("123abc")
time.sleep(5)
driver.find_element(By.XPATH,"//button[@type='button']").click()
time.sleep(5)
driver.quit()