import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os, time


def createWidets():
  
    label1= Label(root, text="Enter The Time     ")
    label1.grid(row=0, column=0, padx=5, pady=5)
    
    global entry1 
    entry1 = Entry(root, width=15)
    entry1.grid(row=0, column=1)
    
    label2= Label(root, text=" Enter The Message ")
    label2.grid(row=1, column=0, padx=5, pady=5)
    
    global entry2
    entry2 = Entry(root, width=15)
    entry2.grid(row=1, column=1)
    
    but = Button(root,text="Sumbit", width=10, command=submit)
    but.grid(row=2,column=1)
    
    global label3
    label3 = Label(root, text="")
    label3.grid(row=3, column=0)
    
def msg1():
    global entry1, label3
    alarmtimelabel = entry1.get()
    label3.config(text=" Counting...")
    messagebox.showinfo("Alarm clock", f"The Alarm time is: {alarmtimelabel}")
    
def submit():
    global entry1, entry2, label3
    alarmtime = entry1.get()
    msg1()
    currenttime =time.strftime("%H:%M")
    alarmmessage = entry2.get()
    print(f" The Alarm time is:{alarmtime }")
    while alarmtime != currenttime:
        currenttime = time.strftime("%H:%M")
        time.sleep(1)
        
    if alarmtime == currenttime:
        print("Playing Alarm Sound...")
        winsound.playsound("*", winsound.SND_ASYNC)
        label3.config(text="Alarm sound Playing>>>")
        messagebox.showinfo("Alam Message",f" the Message is: {alarmmessage}")
        
root = tk.Tk()
root.title (" Alarm clock with GUI")
root.geometry("400x300")



createWidets()

root.mainloop()