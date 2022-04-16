from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://syncnau.poltektegal.ac.id/login")
time.sleep(2)

driver.find_element_by_name("username").send_keys("19090089")
driver.find_element_by_name("password").send_keys("25desember")
driver.find_element_by_id("submit").click()

driver.get("https://syncnau.poltektegal.ac.id/profil")
uploadfoto = driver.find_element_by_xpath("//input[@type='file']")

driver.find_element_by_name("user_foto").send_keys("C:/Users/dasmi/Pictures/IMG_20220304_204907.jpg")
driver.find_element_by_name("simpan_foto").click()

