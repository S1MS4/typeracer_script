import time
import pyautogui
import keyboard
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

def get_text(driver):
    time.sleep(1)
    src = driver.page_source
    soup = BeautifulSoup(src,"html.parser")
    span = soup.findAll("span")
    text = ""

    for i in span:
        if "incomplete current" or "incomplete" in str(i):
            text += i.text

    if not text:
        print("no txt")
        return None
    else:
        print("text to type: ", text)
    return text

def type_text(text):
    pyautogui.typewrite(text)

def main():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://humanbenchmark.com/tests/typing")
    keyboard.wait("CTRL + ALT + 1")

    text_to_type = get_text(driver)
    if text_to_type:
        type_text(text_to_type)

main()