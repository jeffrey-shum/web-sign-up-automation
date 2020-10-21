# sign_up.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import timedelta, datetime

# Creating date variables:
today = datetime.today()
seven_days_from_today = today + timedelta(days=7)
date_string = seven_days_from_today.strftime("%A %B %e")
class_time = "6:15 AM - 7:00 AM"
#TODO: delete after testing:
    #class_time = "7:45 AM - 8:30 AM"
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

# Creating variables for working with Chrome:
xpath_date_sensitive = f"/html/body/div/table/tbody/tr/td[2]/table[2]/tbody/tr/td[{day_var}]/div/div[3]"
#TODO: delete after testing, this is just an example:
    #xpath_date_sensitive = "/html/body/div/table/tbody/tr/td[2]/table[2]/tbody/tr/td[5]/div/div[6]" 
PATH = "/Users/jeff/chromedriver"
driver = webdriver.Chrome(PATH)

def login(login_url):   
    driver.get(login_url)
    elem = driver.find_element_by_id("idUsername")
    elem.send_keys(lst[2][0]) #TODO: add functionality to sign up for multiple users
    elem = driver.find_element_by_id("idPassword")
    elem.send_keys(lst[2][1])
    elem.send_keys(Keys.RETURN)

def sign_up(calendar_url, xpath_date_sensitive):
    driver.get(calendar_url)
    try:
        elem = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath_date_sensitive))
        )
        elem.click()

        # Checks whether the member is already registered for the class:
        if "Jeff Shum is registered for this class" in driver.page_source:             
            print(f"Jeff Shum is already registered for {class_time} Bootcamp class on {date_string}")
        # Checks whether browser is on the correct page:
        elif (date_string in driver.page_source) and (class_time in driver.page_source): 
            try:
                elem = WebDriverWait(driver, 5).until(
                    expected_conditions.element_to_be_clickable((By.ID, "reserve_1"))
                )
                elem.click()
                if "Jeff Shum is registered for this class" in driver.page_source:
                    print(f"Jeff Shum was successfully registered for {class_time} Bootcamp class on {date_string}.")
                else:
                    print("Something went wrong, manually check to see whether the member is signed up for the class.")
            except:
                print("Something went wrong, manually check to see whether the member is signed up for the class.")
        else:
            print("There was a problem. It's likely that the script navigated to the wrong sign-up link.")
    finally:
        driver.quit()

def main():
    login(login_url)
    sign_up(calendar_url, xpath_date_sensitive)

if __name__ == "__main__":
    main()
