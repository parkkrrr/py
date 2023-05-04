from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
from msedge.selenium_tools import EdgeOptions
import time

# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.maximize_window()

# Set the path to the Edge webdriver executable
edge_path = "C:\msedgedriver.exe"

# Create an instance of the EdgeOptions class to configure the browser options
# edge_options = EdgeOptions()
# edge_options.use_chromium = True
# edge_options.add_argument("start-maximized")
# edge_options.add_argument("disable-infobars")
# edge_options.add_argument("--disable-extensions")
# # edge_options.add_argument("--disable-gpu")
# edge_options.add_argument("--disable-dev-shm-usage")
# edge_options.add_argument("--no-sandbox")

# Create a new instance of the Edge browser
browser = webdriver.Edge(executable_path=edge_path)

url = "https://docs.google.com/forms/d/e/1FAIpQLSc4Ch_TCh13dNVlFzohk1pzJEYtUXfTDy4ORz6zevTQxViUTw/viewform"
num_responses = 5
for i in range(num_responses):
    browser.get(url)
    time.sleep(3)

    radio = browser.find_elements_by_class_name("AB7Lab Id5V1")
    checkbox=browser.find_elements_by_class_name("uHMk6b fsHoPb")
    submit=browser.find_elements_by_class_name("l4V7wb Fxmcue")

    radio.click()

    checkbox.click()
    checkbox.click()
    submit.click()
    time.sleep(3)
    # browser.close()




'''for i in range(num_responses):
    browser.get(url)
    time.sleep(3)

    # Find the input fields and fill them in
    input_fields = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
    for field in input_fields:
        # Check if the field is a radio button
        if "Radio" in field.get_attribute("class"):
            # Click on the radio button
            field.click()
            time.sleep(0.5)
    # Submit the form
    submit_button = browser.find_element_by_xpath("//span[contains(text(),'Submit')]")
    submit_button.click()
    time.sleep(3)
    '''


'''
# Use the following snippets to get elements by their class names
textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

# Use the following snippets to get elements by their XPath
otherboxes = browser.find_element_by_xpath("<Paste the XPath here>")

textboxes[0].send_keys("Hello World")

radiobuttons[2].click()

checkboxes[1].click()
checkboxes[3].click()

submitbutton[0].click()

browser.close()
'''