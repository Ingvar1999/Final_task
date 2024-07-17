from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

# Блок c 17.07.2024 г. v 3
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"


# Блок до 17.07.2024 г. v 2
#    def should_be_login_link(self):
#        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"

# Блок до 17.07.2024 г. v 1
#    def should_be_login_link(self):
#        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")