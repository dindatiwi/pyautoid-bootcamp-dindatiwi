from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path='/Users/dindatiwi/Downloads/chromedriver')

driver.get('https://demoqa.com/alerts')
try: 
    driver.find_element_by_id("timerAlertButton").click()
    WebDriverWait(driver,8).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("berhasil")
except TimeoutException:
    print("Gagal melakukan action")
driver.close()