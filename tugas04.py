import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

tobe_inserted = {
    'userName': 'dindatiwi',
    'userEmail': 'tiwiwiw@gmail.com',
    'currentAddress': 'Bumi',
    'permanentAddress': 'Bumi'
}

driver = webdriver.Chrome(executable_path='/Users/dindatiwi/Downloads/chromedriver')
def test_inserted():
    driver.get('https://demoqa.com/text-box')
    driver.implicitly_wait(10)
    for key,info in tobe_inserted.items():
        driver.find_element_by_id(key).send_keys(info)
    driver.find_element_by_id("submit").click()
    try:
        wait = WebDriverWait(driver,5) 
        wait.until(EC.presence_of_element_located((By.ID,"output")))
        print("berhasil menemukan boxElement")
        name_box = wait.until(EC.presence_of_element_located((By.ID,"name")))
        email_box = wait.until(EC.presence_of_element_located((By.ID,"email")))
        cAddress_box = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[6]/div/p[3]')))
        pAddress_box = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[6]/div/p[4]')))
        assert name_box.text == "Name:dindatiwi"
        assert email_box.text == "Email:tiwiwiw@gmail.com"
        assert cAddress_box.text == "Current Address :Bumi"
        assert pAddress_box.text == "Permananet Address :Bumi"
    except TimeoutException:
        print("Gagal melakukan action")
    driver.close()