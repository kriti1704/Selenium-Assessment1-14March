""" Automate Login Process on Facebook Using CSS Selectors
Description
Description
Open the Facebook login page using Selenium WebDriver.
 Maximize the browser window and locate the username/email field and password field using CSS selectors.

Enter sample login credentials into the respective fields and then locate the Login button using a CSS selector and click it.

Use appropriate waits if necessary to ensure elements are loaded before interacting with them.

Expected Outcome
The browser launches successfully.


The Facebook login page opens.


The username/email field is located using a CSS selector and text is entered.


The password field is located using a CSS selector and text is entered.


The Login button is clicked successfully.


The script executes without errors. """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"#_R_1h6kqsqppb6amH1_").send_keys("kritijain617@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#_R_1hmkqsqppb6amH1_").send_keys("Kriti@3421")
sleep(1)
driver.find_element(By.CSS_SELECTOR,"div[aria-label='Log in']").click()
sleep(3)
driver.close()