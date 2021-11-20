from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD
from tkinter import messagebox
import random

window=Tk()
window.geometry("400x350")
window.title("LOGIN")
frame1=Frame(window, pady=20, padx=20)
frame1.pack(anchor='w')

text = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
captcha = StringVar()
input = StringVar()
CheckVar1=IntVar()

def create_captcha():
    c = random.choices(text, k = 6)
    captcha.set(''.join(c))
def check():
    if captcha.get() == input.get():
        messagebox.showinfo('Captcha Verification', 'Captcha verified Succesfully..')
    else:
        messagebox.showerror('Captcha Verification', 'Incorrect Captcha')
    input.set('')
    create_captcha()

regno=Label(frame1,text="USER NAME :",font=('times new roman',14),pady=10)
regnow=StringVar()
passwo=Label(frame1,text="PASSWORD :",font=('times new roman',16),pady=10)
passwow=StringVar()
che=Checkbutton(frame1, text = "STAY SIGNED IN", variable = CheckVar1,pady=10)
code=Label(frame1,text="ENTER THE TEXT YOU SEE ABOVE",font=('times new roman',12),pady=10)
codew=StringVar()
captha=Label(frame1, textvariable=captcha,bg="lightgrey", font=("ariel 16 bold"),pady=10)
btn=Button(frame1, text="SUBMIT", font="ariel 15 bold", bg='gold', command=check)

Eregno=ttk.Entry(frame1,textvariable=regnow, width=25)
Ecode=Entry(frame1, textvariable=input, bg='white', font="ariel 12 bold", width=40)
Epasswo=ttk.Entry(frame1, textvariable=passwow, width=25, show='*')

regno.grid(row=1,column=1,sticky=tk.W)
Eregno.place(x=165,y=14)
passwo.grid(row=3,column=1,sticky=tk.W)
Epasswo.place(x=165,y=62)
che.grid(row=5,column=1,sticky=tk.W)
captha.grid(row=6,column=1)
code.grid(row=7,column=1)
Ecode.grid(row=8,column=1)
btn.grid(row=9,column=1)

create_captcha()
window.mainloop()