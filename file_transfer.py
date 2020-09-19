import shutil
import os
import sys
import time
import datetime
from datetime import timedelta
from datetime import datetime
import tkinter
from tkinter import *
from tkinter import filedialog

source = '' #make these variables

destination =''

def browse_button(self):
    # Allow user to select a directory and store it in global var
    # called folder_path
    source = filedialog.askdirectory()
    folder_path.set(source)
    print(source)
    return source

def getDestination(self):
    destination = filedialog.askdirectory()
    folder_path1.set(destination)
    print(destination)
    return destination

def move_file(self):
    files = os.listdir(self.e1.get())
    source = self.e1.get()
    destination = self.e2.get()
    source = source + "/"
    destination = destination + "/"
    for i in files:
        # Get last modified date and today's date
        modifyDate = datetime.fromtimestamp(os.path.getmtime(source+i))
        todaysDate = datetime.today()
        
        
        # If modified within last 24 hours, then copy to destination folder
        modifyDateLimit = modifyDate + timedelta(hours=24)

        print(modifyDate,todaysDate,modifyDateLimit)
        if modifyDateLimit > todaysDate:
             shutil.copy2(source+i, destination)
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Check Files")

        self.browse_button = Button(master, text="source", command = lambda: browse_button(self))
        self.browse_button.grid(row=1,column=0)

        self.browse_button = Button(master, text="destination", command = lambda: getDestination(self))
        self.browse_button.grid(row=2,column=0)

        self.file_button = Button(master, text="move files", command = lambda: move_file(self))
        self.file_button.grid(row=3,column=0)

        self.filepath = folder_path
        self.filepath1 = folder_path1

        self.e1 = Entry(self.master, text=self.filepath)
        self.e1.grid(row=1,column=1)

        self.e2 = Entry(self.master, text=self.filepath1)
        self.e2.grid(row=2,column=1)
    
        self.close_button = Button(master, text="Close Program", command=master.quit)
        self.close_button.grid(row=3,column=4)



root = Tk()
folder_path = StringVar()
folder_path1 = StringVar()

my_gui = MyFirstGUI(root)
root.mainloop()
