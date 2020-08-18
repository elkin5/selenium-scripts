from selenium import webdriver

driver = webdriver.Chrome(executable_path="drivers/chromedriver")

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.quit()
