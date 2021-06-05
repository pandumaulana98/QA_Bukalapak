from selenium import webdriver

#Installasi chromedriver dan pengarahan link Bukalapak
driver = webdriver.Chrome()
driver.get('https://www.bukalapak.com')

#Input nama barang (contoh: "mouse")
username = driver.find_element_by_name('search[keywords]').send_keys("mouse")

#Submit nama barang yang dicari
submit = driver.find_element_by_class_name('v-omnisearch__submit').click()