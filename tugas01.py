from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/dindatiwi/Downloads/chromedriver')
websites = ["https://noobtest.id","https://erzaf.com","https://orangsiber.com","https://demoqa.com","https://automatetheboringstuff.com"]
for i in websites:
    driver.minimize_window()
    driver.get(i)
    title = i.split("/",2)
    print(title[2]," - ",driver.title)
    driver.close