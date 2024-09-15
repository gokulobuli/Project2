from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager


def test_admin_page_headers():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys("Admin")  # Replace with the admin username

        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys("admin123")  # Replace with the admin password

        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()


        admin_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='menu_admin_viewAdminModule']"))
        )
        admin_menu.click()


        page_title = WebDriverWait(driver, 10).until(
            EC.title_is("OrangeHRM")
        )
        assert page_title, "Page title is not as expected. Expected 'OrangeHRM'."


        headers = {
            "User Management": "//a[text()='User Management']",
            "Job": "//a[text()='Job']",
            "Organization": "//a[text()='Organization']",
            "Qualifications": "//a[text()='Qualifications']",
            "Nationalities": "//a[text()='Nationalities']",
            "Corporate Banking": "//a[text()='Corporate Banking']",
            "Configuration": "//a[text()='Configuration']"
        }

        for header, xpath in headers.items():
            header_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            assert header_element.is_displayed(), f"Header '{header}' is not displayed."
            print(f"Header '{header}' is displayed.")

    finally:
       
        driver.quit()


# Run the test
test_admin_page_headers()
