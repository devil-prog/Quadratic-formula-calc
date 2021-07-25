##########################ON WORKING##########################
#with Gui coming soon
import os
import tkinter as tk
from tkinter import *

class app:
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)    

    def calculate(self, k):
        i = self.b**2
        i = i-4*self.a*self.c
        i = i**0.5

        x = -self.b+i
        x = x/(2*self.a)
        #or
        y = -self.b-i
        y = y/(2*self.a)

        try:
            print(f"{round(x,k)} or {round(y,k)}")
        except:
            print(f"{x} or {y}")

def run():
    a = float(ea.get())
    b = float(eb.get())
    c = float(ec.get())

    a = app(a,b,c)
    a.calculate(2)
    
#making gui

root = tk.Tk()
root.title("Quadratic-formula-calc")
root.iconphoto(FALSE, PhotoImage(file = 'icon.png'))
root.geometry('500x250')
#add Widgets
#Labels
tk.Label(root, text="Enter a:").grid(row=0)
tk.Label(root, text="Enter b:").grid(row=1)
tk.Label(root, text="Enter c:").grid(row=2)

#Entrys
ea = tk.Entry(root)
eb = tk.Entry(root)
ec = tk.Entry(root)

ea.grid(row=0,column=1)
eb.grid(row=1,column=1)
ec.grid(row=2,column=1)

#Button
tk.Button(root,text="Submit", command=run).grid(row=3,column=2,padx=20,pady=20)

root.mainloop()

#delete this later
#coded by Devil-prog