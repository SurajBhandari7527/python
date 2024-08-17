import pyautogui
import time
import pyperclip

time.sleep(4)
pyautogui.hotkey('f11')

result = set()
file_path = 'contact_numbers.txt'

def check(number):
    try:
        pyautogui.click(480, 50)
        time.sleep(1)
        
        
        pyautogui.write(number)
        time.sleep(1)
        
        pyautogui.press('enter')
        time.sleep(1)
        
        pyautogui.click(800, 50, clicks=2)
        time.sleep(1)
        
        pyautogui.click(1600, 434, clicks=3)
        time.sleep(1)
        
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        
        ans = pyperclip.paste()
        result.add(ans)

        print(result)
        
    except pyautogui.FailSafeException:
        print("FailSafe triggered. Exiting the script.")
        return
code='+'


start=8801913939828  #<------- YEHA INITIAL NUMBER LEKHNI '+' BAHEK SABBAI 


end=start+1000
contact_numbers = []#numbers with country code
for i in range(start,end):
        contact_numbers.append(f"{code}{i}")
        
        print(f"{code}{i}")


time.sleep(5)
for i in contact_numbers:
    check(i)
result=list(result)
result.sort()
with open(file_path, 'w') as file:
    for number in result:
        file.write(number + '\n')