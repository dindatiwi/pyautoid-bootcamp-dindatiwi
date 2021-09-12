from selenium import webdriver
driver = webdriver.Chrome(executable_path='/Users/dindatiwi/Downloads/chromedriver')

list_employee = {'person1': {'firstName': 'aa', 'lastName': 'bruh', 'userEmail': 'bruh@mail.com','age': 15,'salary': 1233, 'department': 'bruh'},
     'person2': {'firstName': 'bb', 'lastName': 'dih', 'userEmail': 'dih@asdasdas.com','age': 6,'salary': 3435, 'department': 'dih'},
     'person3': {'firstName': 'cc', 'lastName': 'dah', 'userEmail': 'dahskjagdka@anskd.com','age': 8,'salary': 66778, 'department': 'dah'}}

driver.get('https://demoqa.com/webtables')

for id, info in list_employee.items():
     driver.find_element_by_id("addNewRecordButton").click()
     for key in info:
         driver.find_element_by_id(key).send_keys(info[key])
     driver.find_element_by_id("submit").click()