from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/dindatiwi/Downloads/chromedriver')
websites = ["https://noobtest.id/","https://erzaf.com/","https://www.orangsiber.com/","https://demoqa.com/","https://automatetheboringstuff.com/"]
for i in websites:
    driver.minimize_window()
    driver.get(i)
    print(driver.title)
    driver.close