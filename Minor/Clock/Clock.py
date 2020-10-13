from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p') # print string in this format
    label.config(text=string)
    label.after(1000,time)  # after every 1000 ie 1 sec call time funct

label=Label(root,font=("ds-digital",80),background="white",foreground="dark blue")
label.pack(anchor='center')
time()

mainloop()