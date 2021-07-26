import os
import tkinter as tk
from tkinter import *
import sys

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

        def output(out, ts):            #Output window goes here
            root = tk.Toplevel()
            root.geometry("720x72")
            msg = tk.Label(root, text=out)
            msg.config(font=('Helvetica bold', ts))
            msg.pack()
            print(out)

        try:
            out = str(str(round(x,k)) +  " or "  + str(round(y,k)))
            output(out, 40)
        
        except TypeError:
            out = str(str(x) + " or " + str(y))
            output(out, 14)

        except:
            print(sys.exc_info()[0])


def run():
    a = float(ea.get())
    b = float(eb.get())
    c = float(ec.get())

    a = app(a,b,c)
    a.calculate(2)

def enter(event):
    run()
    
#main window
root = tk.Tk()
root.title("Quadratic-formula-calc")
root.iconphoto(FALSE, PhotoImage(file = 'icon.png'))
root.geometry('500x250')
#add Widgets
#Labels
tk.Label(root, text="Enter a:").grid(row=0)
tk.Label(root, text="Enter b:").grid(row=1)
tk.Label(root, text="Enter c:").grid(row=2)
tk.Label(root, text="press \"x\" to exit").grid(row=3)

#Entrys
ea = tk.Entry(root)
eb = tk.Entry(root)
ec = tk.Entry(root)

ea.grid(row=0,column=1)
eb.grid(row=1,column=1)
ec.grid(row=2,column=1)

#Button
tk.Button(root,text="Submit", command=run).grid(row=3,column=2,padx=20,pady=20)

#keys binded
root.bind('<Return>', enter)
root.bind('x', exit)

root.mainloop()
#coded by Devil-prog