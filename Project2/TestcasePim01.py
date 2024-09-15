from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager


def test_forgot_password():

    driver = webdriver.Chrome()

    try:

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


        forgot_password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Forgot your password?']/a"))
        )
        forgot_password_link.click()


        username_textbox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        assert username_textbox.is_displayed(), "Username textbox is not visible"


        username_textbox.send_keys("Admin")  # Replace with a valid username if necessary


        reset_password_button = driver.find_element(By.XPATH, "//button[text()='Reset Password']")
        reset_password_button.click()


        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='message success fadable']"))
        ).text

        assert "Reset Password link sent successfully" in success_message, "Success message not displayed or incorrect"

        print(f"Success message: {success_message}")

    finally:

        driver.quit()



test_forgot_password()
