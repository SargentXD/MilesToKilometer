import tkinter as tk
from tkinter import ttk
from tkinter import font
import ttkbootstrap as ttk

def convert():
    print("[/] Converting value")
    print(entryInt.get())
    number = entryInt.get()
    number = number * 1.61
    output_str.set(str(number))
    
    

#Main window 
window = ttk.Window(themename = 'darkly')
window.title("Demo")
window.geometry('300x200')

#title
title_lable = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 20 bold')
title_lable.pack()

#inputfeild
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entryInt)
button = ttk.Button(master=input_frame, text="Convert" ,command = convert)
entry.pack(pady=10)
button.pack()
input_frame.pack(pady=10)

#output
output_str = tk.StringVar()
output_lable = ttk.Label(
    master = window, 
    text = 'Output', 
    font='Calibri 24', 
    textvariable = output_str
)

output_lable.pack()


#run 
window.mainloop()

