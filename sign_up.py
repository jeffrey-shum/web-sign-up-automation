# sign_up.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import timedelta, datetime
import time

# Creating date variables:
today = datetime.today()
seven_days_from_today = today + timedelta(days=7)
date_string = seven_days_from_today.strftime("%A %B %e") # %e is the day numner with a space instead of a leading zero
class_time = "6:15 AM - 7:00 AM"
year = str(seven_days_from_today.year)
month = str(seven_days_from_today.month)
day = str(seven_days_from_today.day)
day_var = today.weekday() + 3 #this is used to compose the xpath to the sign-up link depending on what day of the week it is


# Processing data from text file:
with open("/Users/jeff/cfamatak_automation/data.txt") as file:
    lines = file.readlines()
    lst = []
    for line in lines:
        line = line.strip().split(',')
        lst.append(line)
    login_url = lst[0][1]
    calendar_url = lst[1][1] + f"{year}-{month}-{day}"


# Setting up xpath and Chrome webdriver
xpath_date_sensitive_615AM = f"/html/body/div/table/tbody/tr/td[2]/table[2]/tbody/tr/td[{day_var}]/div/div[3]"
PATH = "/Users/jeff/chromedriver"
driver = webdriver.Chrome(PATH)

def login(login_url):   
    driver.get(login_url)
    elem = driver.find_element_by_id("idUsername")
    elem.send_keys(lst[2][0]) #TODO: add functionality to sign up for multiple users
    elem = driver.find_element_by_id("idPassword")
    elem.send_keys(lst[2][1])
    elem.send_keys(Keys.RETURN)

#TODO: the code below is a starting point for running Javascript
    # this is a potential solution for inability to click 715AM class

    #IJavaScriptExecutor ex = (IJavaScriptExecutor)Driver;
    #ex.ExecuteScript("arguments[0].click();", elementToClick);
    #
    #execute_script(script, *args)
    #Synchronously Executes JavaScript in the current window/frame.
    #
    #Args:   
    #    script: The JavaScript to execute.
    #    *args: Any applicable arguments for your JavaScript.
    #    Usage:  
    #        driver.execute_script(‘return document.title;’)


def sign_up(calendar_url, xpath_date_sensitive):
    driver.get(calendar_url)
    try:
        elem = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath_date_sensitive))
        )
        #TODO: enable functionality to click on 7:15AM class elements:
            #driver.execute_script("arguments[0].click;", elem)
        elem.click()

        try:
            elem = WebDriverWait(driver, 5).until(
                expected_conditions.element_to_be_clickable((By.ID, "reserve_1"))
            )
            time.sleep(5)
            elem.click()
            print(f"Member was successfully registered for {class_time} Bootcamp class on {date_string}.")
        except:
            print("Something went wrong, manually check to see whether the member is signed up for the class.")
    finally:
        driver.quit()

def main():
    login(login_url)
    sign_up(calendar_url, xpath_date_sensitive_615AM)

if __name__ == "__main__":
    main()
