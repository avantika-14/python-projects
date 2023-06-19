import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os,time,winsound

def createWidgets():

    l1=Label(root,text="Enter time in hh:mm format:\t")
    l1.grid(row=0,column=0,padx=5,pady=5)
    global entry1 #text inside entry1 will be used globally
    entry1=Entry(root,width=15)
    entry1.grid(row=0,column=1)

    l2=Label(root,text="Enter message for alarm:\t")
    l2.grid(row=1,column=0,padx=5,pady=5)
    global entry2 
    entry2=Entry(root,width=15)
    entry2.grid(row=1,column=1)

    b1=Button(root,text="Submit",width=10,command=submit)
    b1.grid(row=2,column=1)

    global l3
    l3=Label(root,text="")
    l3.grid(row=3,column=0)

def messageb():
    global entry1,l3
    Alarmtimelabel=entry1.get()
    l3.config(text="Alarm is set")
    messagebox.showinfo("Alarm Clock",f"The Alarm time is:{Alarmtimelabel}")

def submit():
    global entry1,entry2,l3
    Alarmtime=entry1.get()
    messageb()
    currenttime=time.strftime("%H:%M")
    am=entry2.get()
    print(f"The Alarm time is:{Alarmtime}")
    while Alarmtime!=currenttime:
        currenttime=time.strftime("%H:%M")
        time.sleep(1)
    if Alarmtime==currenttime:
        print("Timesup!")
        winsound.PlaySound("*",winsound.SND_ASYNC)
        l3.config(text="its time")
        messagebox.showinfo("Alarm Message",f"The message is:{am}")
              
#interpreter instance
root=tk.Tk()
root.title("Alarm Clock")
root.geometry("400x150")

#calling the function
createWidgets()

root.mainloop()
