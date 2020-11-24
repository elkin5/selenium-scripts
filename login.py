from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver")

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(5)
# Se obtienen los elementos del login
username = driver.find_element_by_id("txtUsername")
password = driver.find_element_by_id("txtPassword")
login_btn = driver.find_element_by_id("btnLogin")

# Se agregan los valores a los respectivos campos
username.send_keys("Admin")
password.send_keys("admin123")

# Dar clieck sobre el boton
login_btn.click()

driver.quit()