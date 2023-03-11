
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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
time.sleep(20)

# Close the browser
browser.close()