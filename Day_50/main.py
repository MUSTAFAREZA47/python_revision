import os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Replace with your credentials (use env or secure store in real apps)
GOOGLE_ACCOUNT_EMAIL = "youremail@gmail.com"
GOOGLE_ACCOUNT_PASSWORD = "yourpassword"

class TinderAutoSwipe:
    def __init__(self):
        # Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--lang=en")
        chrome_options.add_argument(f"--user-data-dir={os.getcwd()}/.data")  # persist session
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

        self.main_frame = ""
        self.login_frame = ""

    def login(self):
        self.driver.get("https://tinder.com/")
        sleep(5)

        # Save the main window handle
        self.main_frame = self.driver.current_window_handle

        # Accept cookies if present
        try:
            cookies_button = self.driver.find_element(By.XPATH, '//*[text()="I accept"]')
            cookies_button.click()
            sleep(1)
        except NoSuchElementException:
            pass

        # Click on login button
        try:
            login_button = self.driver.find_element(By.XPATH, '//*[text()="Log in"]')
            login_button.click()
            sleep(5)
        except NoSuchElementException:
            pass

        # Attempt to switch to Google login iframe
        try:
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH, '//*[@title="Sign in with Google Button"]'))
            google_sign_in_button = self.driver.find_element(By.XPATH, '//*[@role="button"]')
            google_sign_in_button.click()
            sleep(5)
        except NoSuchElementException:
            pass

        # Switch to new window for Google login
        for handle in self.driver.window_handles:
            if handle != self.main_frame:
                self.login_frame = handle
                self.driver.switch_to.window(self.login_frame)

        # Google login: email
        try:
            google_mail = self.driver.find_element(By.ID, 'identifierId')
            google_mail.send_keys(GOOGLE_ACCOUNT_EMAIL)
            google_mail.send_keys(Keys.ENTER)
            sleep(3)
        except NoSuchElementException:
            pass

        # Google login: password
        try:
            google_password = self.driver.find_element(By.XPATH, '//*[@name="password"]')
            google_password.send_keys(GOOGLE_ACCOUNT_PASSWORD)
            google_password.send_keys(Keys.ENTER)
            sleep(10)
        except NoSuchElementException:
            pass

    def swipe(self):
        self.driver.switch_to.window(self.main_frame)

        for i in range(100):  # swipe 100 times
            try:
                # Close 'Add to Home Screen' popup if exists
                popup = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add Tinder to your Home Screen')]")
                dialog = self.driver.find_element(By.XPATH, '//*[@role="dialog"]')
                with open("add_tinder_to_home_screen.html", "w") as f:
                    f.write(dialog.get_attribute('innerHTML'))
                # Ideally click "No Thanks" or close button here
            except NoSuchElementException:
                pass

            try:
                # Find the swipe buttons (like, nope, super like)
                buttons = self.driver.find_elements(By.XPATH, '//button[@aria-label="Like"]')
                if buttons:
                    buttons[0].click()
                    print(f"✅ Swiped right [{i+1}/100]")
                else:
                    print("⚠️ Like button not found.")
            except NoSuchElementException:
                print("❌ Error finding card or button")

            sleep(2)

if __name__ == '__main__':
    app = TinderAutoSwipe()
    app.login()
    app.swipe()
