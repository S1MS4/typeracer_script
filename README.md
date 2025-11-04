# Human Benchmark Typing Test Auto-Typer

This script automates the [Human Benchmark Typing Test](https://humanbenchmark.com/tests/typing) by scraping the text to type from the webpage and automatically typing it using your keyboard.

## ⚠️ Disclaimer
This script is for educational purposes only. Automating human performance tests violates the spirit of fair play and may breach the site's terms of service. Use responsibly and at your own risk.

## Features
- Automatically opens the Human Benchmark Typing Test in Chrome
- Waits for your manual trigger (`Ctrl + Alt + 1`) before starting
- Scrapes the text to be typed from the webpage
- Automatically types the text at high speed

## Requirements
- Python 3.x
- Chrome browser
- ChromeDriver (must match your Chrome version)

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install required packages:
   ```bash
   pip install selenium beautifulsoup4 pyautogui keyboard
   ```

3. Download and install [ChromeDriver](https://chromedriver.chromium.org/) and ensure it's in your system PATH.

## Usage
1. Run the script:
   ```bash
   python typing_bot.py
   ```

2. A Chrome window will open and navigate to the typing test page.

3. When you're ready to start, press **Ctrl + Alt + 1**.

4. The script will automatically type the text and submit it.

## How It Works
1. Uses Selenium to control Chrome and load the typing test page
2. Parses the page HTML with BeautifulSoup to extract the text to type
3. Uses PyAutoGUI to simulate keyboard typing
4. Waits for a manual trigger key combination to prevent accidental execution

## Limitations
- May not work if the website structure changes
- Requires the browser window to be in focus during typing
- Accuracy and WPM scores may be affected by system performance

## License
This project is for educational purposes only. Not affiliated with Human Benchmark.
