from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/dindatiwi/Downloads/chromedriver')
websites = ["https://noobtest.id","https://erzaf.com","https://orangsiber.com","https://demoqa.com","https://automatetheboringstuff.com"]
driver.minimize_window()
for i in websites:
    driver.get(i)
    title = i.split("/")
    print(title[2], " - ", driver.title)
driver.close()
