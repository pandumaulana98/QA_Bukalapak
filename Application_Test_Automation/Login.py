from selenium import webdriver

#Inisiasi username dan password
username = "089610244771"
password = "kentut62"

#Installasi chromedriver dan pengarahan link Bukalapak
driver = webdriver.Chrome()
driver.get('https://www.bukalapak.com')

#Klik login pada landing page
login1 = driver.find_element_by_link_text('Login').click()

#Input username dan password pada form login
username = driver.find_element_by_name('user_session[username]').send_keys(username)
pw = driver.find_element_by_name('user_session[password]').send_keys(password)

#Submit username dan password
login2 = driver.find_element_by_name('commit').click()