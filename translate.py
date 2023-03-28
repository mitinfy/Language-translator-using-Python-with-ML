#pip install translate
from translate import Translator
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
root=tk.Tk()
root.geometry('300x500')
root.title('Language Translator')

img = ImageTk.PhotoImage(Image.open("langtrans.jpg"))
lbi=tk.Label(root, image=img).pack()

hd=Label(root, text='Language Translator', font='sans 14', bg='yellow', fg='blue').pack(fill='both')
l1=Label(root, text='From', font='sans 14 bold').pack()
e1=Entry(root, font='sans 14 bold')
e1.pack()

l2=Label(root, text='To',font='sans 14 bold').pack()
e2=Entry(root,font='sans 14 bold')
e2.pack()

l3=Label(root, text='Enter text', font='sans 14 bold').pack()
e3=Entry(root,font='sans 14 bold')
e3.pack()

#l4=Label(root, text='Output').pack()
#e4=Entry(root).pack()

def trans():
    t1=e1.get()
    t2=e2.get()
    t3=e3.get()
    translator= Translator(from_lang=t1, to_lang=t2)
    translation = translator.translate(t3)
    lb=Label(root, bg="cyan", text=translation)
    lb.pack()
    print (translation)

b1=Button(root, text='Submit', command=trans,font='sans 12', bg='blue', fg='yellow').pack(fill='both')

root.mainloop() 
