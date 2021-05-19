from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.chrome.options import Options
import time 

#Getting Chrome Driver and setting profile settings
options1 = Options()
options1.add_argument(r"--user-data-dir=C:\Users\Ayoub\AppData\Local\Google\Chrome\User Data 1")
options1.add_argument(r'--profile-directory=Profile 1')
browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",options=options1)


#Load page
browser.get("https://google.com/search?q=python")

#Wait to find element in page
first_result = ui.WebDriverWait(browser, 15).until(lambda browser: browser.find_element_by_class_name('eKjLze'))
first_link = first_result.find_element_by_tag_name('a')

# Save the window opener (current window, do not mistaken with tab... not the same)
main_window = browser.current_window_handle

# Open the link in a new tab by sending key strokes on the element
# Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack 
first_link.send_keys(Keys.CONTROL + Keys.RETURN)

# Switch tab to the new tab, which we will assume is the next one on the right
browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
time.sleep(2)

# Put focus on current window which will be the window opener
browser.switch_to.window(main_window)
time.sleep(2)

# Switch window handles
browser.switch_to.window(browser.window_handles[1])

# Do stuff with buttons
#browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')


