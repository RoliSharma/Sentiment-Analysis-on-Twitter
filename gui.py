import tkinter as tk
from tkinter import Label,Entry,PhotoImage #,Canvas,Frame

def value():
    title=submit()
    return title

def submit():
    title=value.get()
    print(title)
    r.destroy()
    return title


r = tk.Tk()     #r is the main window
r.geometry("500x200")
bg = PhotoImage( file = "frame.png")
value=tk.StringVar(r)
r.title('Sentiment Analysis on Twiiter'); 
L1 = Label(r, text="Enter topic name")
L1.pack()
E1 = Entry(r,textvariable=value, bd =5)
E1.pack()
button = tk.Button(r,bg="#3f78c4" ,fg="#e8faf1",bd=0,font="Sans-Serif",activeforeground="#1458b3",activebackground="#e8faf1",text='Submit', width=50, command=submit) 
button.pack() 
r.mainloop()     #run the main window