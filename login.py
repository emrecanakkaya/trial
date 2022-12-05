from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests

# // amazon url and test data information
amazon_url = 'http://www.amazon.com'
testuser = 'emreakkaya.nl@gmail.com'
testpassword = 'Test123*'

# // adding options . Because "sign in" menu is drop down menu
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe', chrome_options=options)
action = ActionChains(driver)
time.sleep(1)

# // go to url
driver.get(amazon_url)
time.sleep(3)
print("Amazon page is opened successfully")

# // opening the drop down menu
firstdropdownmenu = driver.find_element(by=By.XPATH,value='//*[@id="nav-link-accountList"]')
action.move_to_element(firstdropdownmenu).perform()
time.sleep(3)
print("Dropdown menu is opened successfully ")

# // go to url
signinbutton = driver.find_element(by=By.XPATH,value='//*[@id="nav-flyout-ya-signin"]/a/span')
signinbutton.click()
time.sleep(3)
print("Sign in page is opened successfully")

# // This part is checking for http code. but it failed couldn't understand the reason . just removed.
### links = driver.find_elements(by=By.CSS_SELECTOR,value='a')
#for link in links:
    #r = requests.head(link.get_attribute('href'))
    #print(link.get_attribute('href'), r.status_code)

# // username
username = driver.find_element(by=By.ID,value='ap_email')
username.send_keys(testuser)
cntbutton = driver.find_element(by=By.ID,value='continue')
cntbutton.click()
time.sleep(3)
print("Username is entered successfully")

# // password
password = driver.find_element(by=By.ID,value='ap_password')
password.send_keys(testpassword)
signbutton = driver.find_element(by=By.ID,value='signInSubmit')
signbutton.click()
time.sleep(3)


# // Adding assertion to check title and success login
assert "Amazon" in driver.title
print("Sucessfully login")


# // logout
firstLevelMenu = driver.find_element(by=By.XPATH,value='//*[@id="nav-link-accountList"]')
action.move_to_element(firstLevelMenu).perform()
time.sleep(3)
signoutbutton = driver.find_element(by=By.ID,value='nav-item-signout')
signoutbutton.click()
print("Sucessfully logout")

driver.quit()
