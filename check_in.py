# check_in.py
# URL for calendar: https://crossfitamatak.sites.zenplanner.com/calendar.cfm
# URL again with arguments: https://crossfitamatak.sites.zenplanner.com/calendar.cfm?DATE=2020%2D10%2D14&VIEW=month&PERSONID=E808BD6B%2DFF80%2D4E7A%2D91EF%2D8A840CF1CC4C

from selenium import webdriver
PATH = "/cfamatak-automation/chromedriver"

driver = webdriver.Chrome(PATH)
driver.get("https://google.com")
print(driver.title)
driver.quit()
