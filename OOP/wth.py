import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

# Initialize the WebDriver (assuming you are using Chrome)
driver = webdriver.Chrome()


# List of phone numbers to check
initial_number=8801913939878 #<------yesma suruko number rakha ani change gardai jaau 100 ota complete vayesi jaha samma hunxa

final_number=initial_number+101

# Coordinates of the search button
search_button_x = 1900
search_button_y = 80

# Function to detect the search button using PyAutoGUI
def detect_search_button(template_path, save_path):
    # Take a screenshot using PyAutoGUI and search for the button
    button_location = pyautogui.locateOnScreen(template_path, region=(search_button_x - 50, search_button_y - 50, 100, 100), confidence=0.8)
    if button_location:
        screenshot = pyautogui.screenshot()
        screenshot.save(save_path)
        
        # Print the saved screenshot path
        print(f"Search button detected and screenshot saved in: {save_path}")
    else:
        print("Search button not detected")

# Define the save path
save_path = r'C:\Users\Suraj Bhandari\OneDrive\Pictures\Screenshots\detected.png'


for number in range(initial_number,final_number):
    url = f"https://wa.me/+{number}"
    webbrowser.open(url)
    time.sleep(3)
    # Example usage
    detect_search_button('search_button.png', save_path)
    time.sleep(3)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'tab')
    pyautogui.hotkey('ctrl', 'w')
    