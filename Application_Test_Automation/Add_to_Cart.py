from selenium import webdriver

#Installasi chromedriver dan pengarahan link Bukalapak
driver = webdriver.Chrome()
driver.get('https://www.bukalapak.com')

#Input nama barang (contoh: "mouse")
item_name = driver.find_element_by_name('search[keywords]').send_keys("mouse")

#Submit nama barang yang dicari
submit_item = driver.find_element_by_class_name('v-omnisearch__submit').click()

#Klik detail barang yang dipilih
search = driver.find_element_by_class_name('bl-thumbnail--img').click()

#Masukkan keranjang
keranjang = driver.find_element_by_class_name('c-main-product__action__cart bl-button bl-button--outline bl-button--medium').click()