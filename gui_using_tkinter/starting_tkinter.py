from tkinter import *
from PIL import ImageTk, Image
import webbrowser
import time
import pyautogui
import os
import sys
import pyperclip

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_path, relative_path)
    print(f"Resource path: {full_path}")  # Debug print
    return full_path



def automate():
    import pyautogui
    import time
    time.sleep(4)
    pyautogui.hotkey('f11')

    result = set()
    file_path = 'C:/Users/Suraj Bhandari/OneDrive/Desktop/list_of_numbers.txt'

    def check(number):
            try:
                pyautogui.click(550, 50)
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
                
                pyautogui.click(135, 50)


                print(result)
                
            except pyautogui.FailSafeException:
                print("FailSafe triggered. Exiting the script.")
                return
    code='+'


    start=int(box.get())  


    end=start+int(To_add.get())
    contact_numbers = []#numbers with country code
    for i in range(start,end):
            contact_numbers.append(f"{code}{i}")
            
            print(f"{code}{i}")


    time.sleep(5)
    for i in contact_numbers:
        check(i)
    result=list(result)
    for i in result:
        print(i)
    result.sort()
    print('The numbers are: ',result)
    with open(file_path, 'a') as file:
        for number in result:
            file.write(number+'\n')
            


root = Tk()
root.title('Whatsapp automation')
root.iconbitmap(resource_path('IMAGES FOR GUI/Automation.ico'))
root.minsize(800, 450)
root.geometry('800x480')
root.configure(background='#F5F5DC')

# pip install pillow to install PIL (import on line 2)
img = Image.open(resource_path('IMAGES FOR GUI/logo.png'))
resized_img = img.resize((110, 80))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=img)
img_label.pack(pady=(15, 0))

text_label = Label(root, text='Whatsapp Automation', fg='#808080', bg='#F5F5DC')
text_label.pack(pady=(0, 0))
text_label.config(font=('times new roman', 24))



enter_label = Label(root, text='Enter the initial number after "+"', fg='#030764', bg='#F5F5DC')
enter_label.pack(pady=(20, 10))
enter_label.config(font=('times new roman', 14))

box = Entry(root, width=30)
box.pack(pady=(10, 10))
box.config(font=('times new roman', 18))

enter_label1 = Label(root, text='HOW MANY NUMBERS TO CHECK?', fg='#030764', bg='#F5F5DC')
enter_label1.pack(pady=(20, 10))
enter_label1.config(font=('times new roman', 14))

To_add = Entry(root, width=10)
To_add.pack(pady=(10, 10))
To_add.config(font=('times new roman', 18))



automate_btn = Button(root, text='Automate', fg='#000000', bg='#C5C9C7', command=automate)
automate_btn.pack(pady=(10, 5))
automate_btn.config(font=('SIGNIKA', 16))

text_label = Label(root, text='BY SURAJ BHANDARI', fg='#808080', bg='#F5F5DC')
text_label.pack(pady=(10, 5))
text_label.config(font=('times new roman', 12))

root.mainloop()
