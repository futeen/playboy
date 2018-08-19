from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')   # on windows

driver = webdriver.Chrome(chrome_options=chrome_options,
                           executable_path="/Users/futeen/Downloads/chrome driver/chromedriver")
# data = brows
driver.get("https://www.google.com")
lucky_button = driver.find_element_by_css_selector("[name=btnI]")
lucky_button.click()

# capture the screen
driver.get_screenshot_as_file("capture.png")
