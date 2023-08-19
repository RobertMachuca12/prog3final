import unittest
from selenium import webdriver

class TestLoginAutomation(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='path_to_chromedriver.exe')
        self.driver.maximize_window()
        self.base_url = "https://habitoxpert.com"  

    def test_login_valid_credentials(self):
      
        self.driver.get(self.base_url + "/login")

    s
        email_input = self.driver.find_element_by_id("email")
        password_input = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_id("login-button")

        email_input.send_keys("usuario@example.com")
        password_input.send_keys("contraseña123")
        login_button.click()

   
        welcome_message = self.driver.find_element_by_css_selector(".welcome-message")
        self.assertEqual(welcome_message.text, "¡Bienvenido a Habitoxpert!")

    def tearDown(self):
 
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
