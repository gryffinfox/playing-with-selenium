import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = '/home/magdalena/bin/chromedriver'
browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/trial-of-the-stones')

# Riddle of Stones
# Accessing the element of the input box, inserting the password "rock"
riddle_stone = "input[id='r1Input']"
input_element = browser.find_element(By.CSS_SELECTOR,
                riddle_stone).send_keys("rock")
# Sending the answer by clicking on button1
stone_button = "button[id='r1Btn']"
stone_button = browser.find_element(By.CSS_SELECTOR,
                stone_button).click()

# Riddle of Secrets
# Accessing the element of password, copying actual password
password = "div[id='passwordBanner']"
password = browser.find_element(By.CSS_SELECTOR, password).text
# Inserting the password in the second input box
# Using another way how to type the identification for web element
input_password = "input[id='r2Input']"
input_password = browser.find_element(By.CSS_SELECTOR,
                input_password).send_keys(password)
# Sending the answer by clicking on button2
secret_button = "button#r2Butn"
secret_button = browser.find_element(By.CSS_SELECTOR,
                secret_button).click()


# The Two Merchants

richest_merchant = "//b[contains(text(), 'Jessica')]"
richest_merchant = browser.find_element(By.XPATH, richest_merchant).text

input_name = "input[id='r3Input']"
input_element = browser.find_element(By.CSS_SELECTOR,
                input_name).send_keys(richest_merchant)

merchant_button = "button[id='r3Butn']"
merchant_button = browser.find_element(By.CSS_SELECTOR,
                    merchant_button).click()

check_answers = "button[id='checkButn']"
check_answers = browser.find_element(By.CSS_SELECTOR,
                check_answers).click()




#driver.quit()