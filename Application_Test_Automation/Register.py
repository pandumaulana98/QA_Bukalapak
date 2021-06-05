from selenium import webdriver

#Installasi chromedriver dan pengarahan link Bukalapak
driver = webdriver.Chrome()
driver.get('https://www.bukalapak.com')

#Klik login pada landing page
login1 = driver.find_element_by_link_text('Login').click()

#Menuju register page
daftar1 = driver.find_element_by_link_text('Daftar sekarang').click()

#Untuk register melalui FB
#fb = driver.find_element_by_link_text('Facebook').click()

#Untuk register melalui Google
# google = driver.find_element_by_link_text('Google').click()

#Untuk register dengan email/nomor hp
nomorhp = driver.find_element_by_class_name('bl-text-field__input')
nomorhp.send_keys('pandumaulana@gmail.com')

#Jika memilih register dengan email/nomor hp, gunakan ini untuk submit
daftar2 = driver.find_element_by_xpath('//button').click()

#Jika memilih register dengan email/nomor hp, gunakan ini untuk konfirmasi email/nomor hp
konfirmasi = driver.find_element_by_class_name('bl-text bl-text--body-default bl-text--semi-bold bl-text--inverse').click()