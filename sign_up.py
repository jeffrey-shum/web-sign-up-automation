# sign_up.py

# URL for calendar: https://crossfitamatak.sites.zenplanner.com/calendar.cfm
# URL for calendar set to month view: https://crossfitamatak.sites.zenplanner.com/calendar.cfm?DATE=2020%2D10%2D15&VIEW=month
# URL again with arguments: https://crossfitamatak.sites.zenplanner.com/calendar.cfm?DATE=2020%2D10%2D14&VIEW=month&PERSONID=E808BD6B%2DFF80%2D4E7A%2D91EF%2D8A840CF1CC4C

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import timedelta, datetime
from time import sleep

today = datetime.today()
seven_days_from_today = today + timedelta(days=7)
date_string = seven_days_from_today.strftime("%A %B %e")
year = str(seven_days_from_today.year)
month = str(seven_days_from_today.month)
day = str(seven_days_from_today.day)
day_var = today.weekday() + 3 #this is used to compose the xpath to the sign-up link depending on what day of the week it is

login_url = "https://crossfitamatak.sites.zenplanner.com/login.cfm"
my_person_id = "personId=E808BD6B-FF80-4E7A-91EF-8A840CF1CC4C"
xpath_date_sensitive = f"/html/body/div/table/tbody/tr/td[2]/table[2]/tbody/tr/td[{day_var}]/div/div[3]"
#xpath_tues = "/html/body/div/table/tbody/tr/td[2]/table[2]/tbody/tr/td[4]/div/div[3]"
#xpath = "/html/body/div/table/tbody/tr/td/table/tbody/tr/td/div"
#xpath2 = "/html/body/div/table/tbody/tr/td/table/tbody/tr" #this should return 2 elements
url = f"https://crossfitamatak.sites.zenplanner.com/calendar.cfm?DATE={year}-{month}-{day}"
#test_url = "https://crossfitamatak.sites.zenplanner.com/calendar.cfm?DATE=2020-10-15&VIEW=month"
PATH = "/Users/jeff/chromedriver"
driver = webdriver.Chrome(PATH)

def login(login_url):   
    driver.get(login_url)
    elem = driver.find_element_by_id("idUsername")
    elem.send_keys("username")
    elem = driver.find_element_by_id("idPassword")
    elem.send_keys("password")
    elem.send_keys(Keys.RETURN)

def sign_up(url, xpath, sign_up_date):
    driver.get(url)
    try:
        elem = driver.find_element_by_xpath(xpath)
        elem.click()

        print(date_string) 
        if date_string in driver.page_source:
            print("found date string in the page source!")
            elem = WebDriverWait(driver, 5).until(
                expected_conditions.element_to_be_clickable((By.ID, "reserve_1"))
            )
            elem.click()
            print("Attempted to find and click reserve button")
    finally:
        driver.quit()

