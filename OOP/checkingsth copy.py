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
phone_numbers=[
  '+8801913939828', 
    '+8801913939829', '+8801913939830', '+8801913939831', '+8801913939832', 
    '+8801913939833', '+8801913939834', '+8801913939835', '+8801913939836', 
    '+8801913939837', '+8801913939838', '+8801913939839', '+8801913939840', 
    '+8801913939841', '+8801913939842', '+8801913939843', '+8801913939844', 
    '+8801913939845', '+8801913939846', '+8801913939847', '+8801913939848', 
    '+8801913939849', '+8801913939850', '+8801913939851', '+8801913939852', 
    '+8801913939853', '+8801913939854', '+8801913939855', '+8801913939856', 
    '+8801913939857', '+8801913939858', '+8801913939859', '+8801913939860', 
    '+8801913939861', '+8801913939862', '+8801913939863', '+8801913939864', 
    '+8801913939865', '+8801913939866', '+8801913939867', '+8801913939868', 
    '+8801913939869', '+8801913939870', '+8801913939871', '+8801913939872', 
    '+8801913939873', '+8801913939874', '+8801913939875', '+8801913939876', 
    '+8801913939877', '+8801913939878', '+8801913939879', '+8801913939880', 
    '+8801913939881', '+8801913939882', '+8801913939883', '+8801913939884', 
    '+8801913939885', '+8801913939886', '+8801913939887', '+8801913939888', 
    '+8801913939889', '+8801913939890', '+8801913939891', '+8801913939892', 
    '+8801913939893', '+8801913939894', '+8801913939895', '+8801913939896', 
    '+8801913939897', '+8801913939898', '+8801913939899', '+8801913939900', 
    '+8801913939901', '+8801913939902', '+8801913939903', '+8801913939904', 
    '+8801913939905', '+8801913939906', '+8801913939907', '+8801913939908'
]



for number in phone_numbers:
    url = f"https://web.whatsapp.com/send?phone={number}"
    webbrowser.open(url)
    time.sleep(60)
    pyautogui.click(821.25,947.5)
    time.sleep(2)
    pyautogui.click(1627.5,575)
    pyautogui.click(1627.5,575)
    pyautogui.click(1627.5,575)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'tab')
    pyautogui.hotkey('ctrl', 'w')
   
    