""" Open the Naukri.com website using Selenium WebDriver.
 Navigate to the registration page and identify the text input fields such as Name, Email, and Password.

Use the ID locator strategy to locate these elements and enter appropriate sample data into each field using Selenium commands.

Students should ensure that the browser opens successfully, elements are identified correctly, and the values are entered into the fields.

Expected Outcome
The browser launches successfully.


The Naukri registration page opens.


Text is entered into the Name, Email, and Password fields using By.ID.


The fields should visibly contain the entered data after script execution. """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.naukri.com/registration/createAccount?othersrcp=23531&wExp=N&utm_source=google&utm_medium=cpc&utm_campaign=Brand_Login_Register&gclsrc=aw.ds&gad_source=1&gad_campaignid=21008292163&gbraid=0AAAAADLp3cECCLLLvCT-8GvFbYowKRRgP&gclid=EAIaIQobChMI48OA7oOfkwMV12hIAB1PsCaCEAAYASAAEgJ6A_D_BwE")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"name").send_keys("Kriti")
driver.find_element(By.ID,"email").send_keys("kritijain617@email.com")
driver.find_element(By.ID,"password").send_keys("kriti@123")
sleep(4)
driver.close()