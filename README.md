# 🚀 Auto-Text-Typer for Human Benchmark Typing Test 🎯

This Python script automates the typing test on the [Human Benchmark](https://humanbenchmark.com/tests/typing) website. Using a combination of **Selenium**, **BeautifulSoup**, **PyAutoGUI**, and **Keyboard**, it extracts the text to type from the page and simulates typing it.

---

## ✨ Features

- 🌐 Automatically navigates to the **Human Benchmark Typing Test**.
- ✍️ Extracts the text to type from the page in a smart way.
- ⏱ Waits for a user-defined key combination (`CTRL + ALT + 1`) to start typing.
- 🎮 Uses **PyAutoGUI** to simulate typing the extracted text into the input field.
- 👨‍💻 Inspired by **The-CodingSloth** for automating repetitive tasks.

---

## 🛠 Requirements

To run this script, you need to have the following Python packages installed:

- 🐍 Python 3.x
- **Selenium**: Automates browser interaction.
- **BeautifulSoup4**: Parses HTML content and extracts the necessary text.
- **PyAutoGUI**: Simulates keyboard inputs to type the extracted text.
- **Keyboard**: Listens for specific keyboard input events.

You can install all the required packages using `pip`:

```bash
pip install selenium beautifulsoup4 pyautogui keyboard
```

In addition, make sure Google Chrome and ChromeDriver are installed. The script will automatically manage the WebDriver using Selenium's built-in features.

---

## 🚀 How to Use
- Clone or download this repository to your local machine. 🖥️

- Ensure Google Chrome is installed on your system. 🔥

Run the script:
```bash
python auto_text_typer.py
```
- The script will launch Chrome and navigate to the Human Benchmark Typing Test. 🌐

- Wait for the page to load, and ***accept the cookie consent banner***

- Press CTRL + ALT + 1 to trigger the typing automation. ⌨️

- The script will automatically extract the text that needs to be typed and start typing it into the input field. 📝
---

## 📝 Final Thoughts

This is my **first project on GitHub**! 🎉 The code is a bit **sloppy**, but I’m learning and improving. Feel free to share any feedback or suggestions!

Thanks for checking it out! 🚀

---
