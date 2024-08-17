from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('Image viewer')
root.iconbitmap('IMAGES FOR GUI/automation.ico')
root.maxsize(700,800)
root.geometry('700x800')
root.configure(background='#000080')

def repeat(L):
 img=Image.open('IMAGES FOR GUI/{}.png'.format((L[0])))
 resized_img=img.resize((700,700))
 img=ImageTk.PhotoImage(resized_img)
 img_label=Label(root,image=img)
 img_label.pack()
 L.pop(0)
 Next_Button=Button(root,text='Next',fg='#FF0000',bg='#E6E6FA',command=repeat(L))
 Next_Button.pack(pady=(15,15))
 Next_Button.config(font=('times new roman',18))

L=[1,2,3,4,5]
Next_Button=Button(root,text='Click to see the photo',fg='#FF0000',bg='#E6E6FA',command=repeat(L))
Next_Button.pack(pady=(15,15))
Next_Button.config(font=('times new roman',18))






root.mainloop()