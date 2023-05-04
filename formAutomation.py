from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set the path to the Edge webdriver executable
edge_path = "C:\msedgedriver.exe"

# Create a new instance of the Edge browser
browser = webdriver.Edge(executable_path=edge_path)

url = "https://docs.google.com/forms/d/e/1FAIpQLSc4Ch_TCh13dNVlFzohk1pzJEYtUXfTDy4ORz6zevTQxViUTw/viewform"

# Fill in the form
browser.get(url)

# Fill in name
name_field = browser.find_element_by_xpath("//input[@aria-label='Name']")
name_field.send_keys("John Doe")

# Fill in email
email_field = browser.find_element_by_xpath("//input[@aria-label='Email address']")
email_field.send_keys("johndoe@example.com")

# Fill in all available questions
questions = browser.find_elements_by_xpath("//div[@role='listitem']")
for question in questions:
    question_text = question.find_element_by_xpath(".//div[contains(@class,'exportQuestionTitle')]").text
    if question_text == "What's your favorite color?":
        # Fill in favorite color
        choice_field = question.find_element_by_xpath(".//div[@role='listbox']")
        choice_field.click()
        choice_option = choice_field.find_element_by_xpath(".//div[@data-value='Blue']")
        choice_option.click()
    elif question_text == "What's your favorite animal?":
        # Fill in favorite animal
        choice_field = question.find_element_by_xpath(".//div[@role='listbox']")
        choice_field.click()
        choice_option = choice_field.find_element_by_xpath(".//div[@data-value='Dog']")
        choice_option.click()
    elif question_text == "What's your favorite food?":
        # Fill in favorite food
        choice_field = question.find_element_by_xpath(".//div[@role='listbox']")
        choice_field.click()
        choice_option = choice_field.find_element_by_xpath(".//div[@data-value='Pizza']")
        choice_option.click()
    elif question_text == "How often do you exercise?":
        # Fill in exercise frequency
        choice_field = question.find_element_by_xpath(".//div[@role='listbox']")
        choice_field.click()
        choice_option = choice_field.find_element_by_xpath(".//div[@data-value='2-3 times a week']")
        choice_option.click()
    elif question_text == "What's your favorite hobby?":
        # Fill in favorite hobby
        hobby_field = question.find_element_by_xpath(".//input[@type='text']")
        hobby_field.send_keys("Playing video games")
    elif question_text == "What's your favorite movie?":
        # Fill in favorite movie
        movie_field = question.find_element_by_xpath(".//textarea[@class='quantumWizTextinputSimpleinputEl']")
        movie_field.send_keys("The Godfather")
    elif question_text == "What's your favorite book?":
        # Fill in favorite book
        book_field = question.find_element_by_xpath(".//textarea[@class='quantumWizTextinputSimpleinputEl']")
        book_field.send_keys("To Kill a Mockingbird")
    else:
        # Fill in a random answer for all other questions
        text_field = question.find_element_by_xpath(".//textarea[@class='quantumWizTextinputSimpleinputEl']")
        text_field.send_keys("This is a random answer.")

# Submit the form
submit_button = browser.find_element_by_xpath("//span[contains(text(),'Submit')
