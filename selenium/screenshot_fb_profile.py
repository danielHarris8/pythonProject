
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from datetime import datetime
now = datetime.now()

# close notification
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")

# Set up the webdriver
browser = webdriver.Chrome(options=options)
browser.get('https://www.facebook.com')

# Find the email and password fields and enter your login credentials
email = browser.find_element("name", "email")
password = browser.find_element("name","pass")
email.send_keys('your_email')
password.send_keys('your_password')

# Click the login button
login_button = browser.find_element("name","login")
login_button.click()


# Wait for a few seconds to let the page load
time.sleep(10)
browser.get('https://www.facebook.com/profile.php')


time.sleep(5)
ele=browser.find_element(By.CLASS_NAME,'x1ja2u2z')
total_height = ele.size["height"]+1000
browser.set_window_size(1920, total_height)
screenshot_path = f"./screenshot_facebook_profile_{now.strftime('%Y%m%d')}.png"
browser.save_screenshot(screenshot_path)

time.sleep(10)

# Close the browser
browser.close()