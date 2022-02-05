from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

passw = os.environ.get("LINKEDIN_PASS")
email = "kiransettyks@gmail.com"
driver_path = "C:\Program Files\selenium_chromedriver_win32\chromedriver.exe"
s = Service(driver_path)
driver = webdriver.Chrome(service=s)
keywords = ["python", "developer", "software", "engineer"]
for j in keywords:
    driver.get(f"https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1&geoId=104035573&keywords={j}&location=South%20Africa")
    driver.maximize_window()

    sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
    sign_in.click()
    time.sleep(0.5)
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(passw)
    driver.find_element(By.CLASS_NAME, "btn__primary--large").click()
    time.sleep(2)
    jobs = driver.find_elements(By.CSS_SELECTOR, "ul.jobs-search-results__list > li.jobs-search-results__list-item")
    for i in jobs:
        i.click()
        time.sleep(2)
        apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
        apply_button.click()
        driver.find_elements(By.CSS_SELECTOR, "div.display-flex button.artdeco-button").click()
        final_button = driver.find_elements(By.CSS_SELECTOR, "div.display-flex button.artdeco-button--primary").click()
        if final_button.find_element(By.TAG_NAME, "span").text != "Submit application":
            a = input()
    driver.close()


