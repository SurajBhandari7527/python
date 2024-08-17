from tkinter import *
from PIL import ImageTk, Image
import webbrowser
import time
import pyautogui
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_path, relative_path)
    print(f"Resource path: {full_path}")  # Debug print
    return full_path



def automate():
    initial_number = int(box.get())
    t = int(timing_entry.get())
    final_number = initial_number + 101

    for number in range(initial_number, final_number):
        url = "https://wa.me/+{}".format(number)
        webbrowser.open(url)
        time.sleep(t)
        pyautogui.hotkey('alt', 'f4')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'tab')
        pyautogui.hotkey('ctrl', 'w')

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

enter_label = Label(root, text='Enter the initial number', fg='#030764', bg='#F5F5DC')
enter_label.pack(pady=(20, 10))
enter_label.config(font=('times new roman', 14))

box = Entry(root, width=45)
box.pack(pady=(10, 10))
box.config(font=('times new roman', 18))

timing = Label(root, text='Timing to close Whatsapp (sec)', fg='#030764', bg='#F5F5DC')
timing.pack()
timing.config(font=('times new roman', 14))

timing_entry = Entry(root, width=20)
timing_entry.pack(pady=(10, 10))
timing_entry.config(font=('times new roman', 15))

automate_btn = Button(root, text='Automate', fg='#000000', bg='#C5C9C7', command=automate)
automate_btn.pack(pady=(10, 5))
automate_btn.config(font=('SIGNIKA', 16))

text_label = Label(root, text='BY SURAJ BHANDARI', fg='#808080', bg='#F5F5DC')
text_label.pack(pady=(10, 5))
text_label.config(font=('times new roman', 12))

root.mainloop()





