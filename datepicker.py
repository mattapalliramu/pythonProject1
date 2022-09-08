import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)  # switch to frame

# driver.find_element(By.XPATH, "//*[@id='datepicker']").send_keys("08/18/2022") #mm/dd/yyyy

year = "2023"
month = "May"
date = "31"

driver.find_element(By.XPATH, "//*[@id='datepicker']").click()  # Opens DatePicker
time.sleep(10)
while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()  # Next arrow
        # driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click() # Previous arrow

# Select Date
dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text == date:
        ele.click()
        break
