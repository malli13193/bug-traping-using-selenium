from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed
driver.get("file:///path/to/index.html")  # Replace with the full path to your HTML file

try:
    # Locate the button and click it
    button = driver.find_element(By.ID, "btn")
    button.click()
    
    # Check the output
    output = driver.find_element(By.ID, "output").text
    if output == "Hello, World!":
        print("Test Passed: Output is correct!")
    else:
        print(f"Test Failed: Output is '{output}', expected 'Hello, World!'")
finally:
    time.sleep(2)  # Pause to see the result (optional)
    driver.quit()
