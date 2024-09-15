from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager


def test_main_menu_validation():

    driver = webdriver.Chrome()

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


        menu_items = {
            "Admin": "//a[@id='menu_admin_viewAdminModule']",
            "PIM": "//a[@id='menu_pim_viewPimModule']",
            "Leave": "//a[@id='menu_leave_viewLeaveModule']",
            "Time": "//a[@id='menu_time_viewTimeModule']",
            "Recruitment": "//a[@id='menu_recruitment_viewRecruitmentModule']",
            "My Info": "//a[@id='menu_pim_viewMyDetails']",
            "Performance": "//a[@id='menu_performance_viewPerformanceModule']",
            "Dashboard": "//a[@id='menu_dashboard_index']",
            "Directory": "//a[@id='menu_directory_viewDirectory']",
            "Maintenance": "//a[@id='menu_maintenance_purgeEmployee']",
            "Buzz": "//a[@id='menu_buzz_viewBuzz']"
        }

        for item, xpath in menu_items.items():
            menu_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            assert menu_element.is_displayed(), f"Menu item '{item}' is not displayed."
            print(f"Menu item '{item}' is displayed.")

    finally:

        driver.quit()



test_main_menu_validation()
