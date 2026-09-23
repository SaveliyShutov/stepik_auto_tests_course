from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Passes on registration1.html, fails with NoSuchElementException on registration2.html
link = "http://suninjuly.github.io/registration1.html"
# link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Fill in only the required fields, using unique selectors
    browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("ivan@example.com")

    # Submit the form
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Wait for the page to load
    time.sleep(1)

    # Check that registration succeeded
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
