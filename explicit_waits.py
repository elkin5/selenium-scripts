from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class ExplicitWaits(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()

    def test_validate_logout(self):
        username = self.driver.find_element(By.ID, "txtUsername")
        password = self.driver.find_element(By.ID, "txtPassword")
        username.send_keys("Admin")
        password.send_keys("admin123")

        login_btn = self.driver.find_element(By.ID, "btnLogin")
        login_btn.click()

        welcome_admin_link = self.driver.find_element(By.LINK_TEXT, "Welcome Admin")
        welcome_admin_link.click()
        wait = WebDriverWait(self.driver, 10)  # Explicit waits
        logout_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        logout_link.click()
        title_login = self.driver.title
        wait.until(EC.title_contains("OrangeHRM"))
        self.assertEqual(title_login, "OrangeHRM")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
