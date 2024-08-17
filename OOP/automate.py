import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import cv2
import numpy as np

# Initialize the WebDriver (assuming you are using Chrome)
driver = webdriver.Chrome()


# List of phone numbers to check
initial_number=8801913939879 
final_number=initial_number+101

# Coordinates of the search button (this may vary, adjust accordingly)
search_button_x = 1900
search_button_y = 80

# Function to detect the search button using OpenCV
def detect_search_button(template_path, save_path):
    # Take a screenshot using PyAutoGUI
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Load the template
    template = cv2.imread(template_path, 0)
    w, h = template.shape[::-1]
    
    # Convert screenshot to grayscale
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    
    # Match the template
    res = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    
    if len(loc[0]) > 0:
        # Save the screenshot if the template is found
        cv2.imwrite(save_path, screenshot)
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
    