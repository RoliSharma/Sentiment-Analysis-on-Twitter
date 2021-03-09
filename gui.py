import tkinter as tk
from tkinter import Label,Entry,PhotoImage #,Canvas,Frame

def close_window():
    global entry
    entry = E.get()
    r.destroy()


r = tk.Tk()     #r is the main window
r.geometry("500x200")
#bg = PhotoImage( file = "frame.png")
value=tk.StringVar(r)
r.title('Sentiment Analysis on Twiiter'); 
L = Label(r, text="Enter topic name")
L.pack()
E = Entry(r,textvariable=value, bd =5)
E.pack()
button = tk.Button(r,bg="#3f78c4" ,fg="#e8faf1",bd=0,font="Sans-Serif",activeforeground="#1458b3",activebackground="#e8faf1",text='Submit', width=50, command=close_window) 
button.pack() 
r.mainloop()     #run the main window

print(entry);