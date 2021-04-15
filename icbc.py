from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
from dotenv import load_dotenv
load_dotenv()

# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())

# Open the Website
icbc_login = "https://onlinebusiness.icbc.com/webdeas-ui/login;type=driver"
browser.get(icbc_login)

# Last name
last_name = os.environ.get("LAST_NAME")
browser.find_element_by_id("mat-input-0").send_keys(last_name)

# drivers licence number
drivers_license_number = os.environ.get("DRIVERS_LICENSE_NUMBER")
browser.find_element_by_id("mat-input-1").send_keys(drivers_license_number)

# keyword
keyword = os.environ.get("KEYWORD")
browser.find_element_by_id("mat-input-2").send_keys(keyword)

# terms and conditions
browser.find_element_by_class_name("mat-checkbox-inner-container").click()

# sign in
browser.find_element_by_xpath('//span[@class="mat-button-wrapper" and contains(text(), "Sign in")]').click()

# Next page

try:
    element = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, '//span[@class="mat-button-wrapper" and contains(text(), "Reschedule appointment")]'))
    )
    element.click()
except:
    browser.quit()

# yes button
browser.find_element_by_xpath('//span[@class="mat-button-wrapper" and contains(text(), "Yes")]').click()
        
# location 



