import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def start_typing_test():
    # Set up the Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Open browser in full screen
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the typing test page
    driver.get("https://humanbenchmark.com/tests/typing")
    time.sleep(3)  # Wait for page to load

    # Extract the letters from the typing test
    letters = driver.find_elements(By.CSS_SELECTOR, ".letters span")
    text_to_type = "".join([letter.text for letter in letters])

    # Find the typing input field
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Type each letter with a small delay to simulate human typing
    for letter in text_to_type:
        input_field.send_keys(letter)
        time.sleep(0.05)  # Adjust speed (50ms per key)

    print("Typing test completed!")
    time.sleep(3)  # Pause to see results before closing
    driver.quit()

# Wait for the Ctrl + Alt + T combination
print("Press Ctrl + Alt + T to start typing...")
keyboard.add_hotkey('ctrl+alt+t', start_typing_test)

# Keep the script running to listen for the key combination
keyboard.wait('esc')  # Press 'Esc' to stop the script
