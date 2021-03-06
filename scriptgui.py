import tkinter
from tkinter import *
from tkinter import filedialog
import webbrowser
def browse_button(self):
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

def html(self):
    header = self.filepath1.get() #grabs the value stored in the second text box and stores it in variable header
    f = open("text.html", "w") #opens an html file or creates one if that file doesnt exist and overwrites its content
    x=("""<html> 
         <body> 
            <h1>
              {} 
           </h1>
         </body> 
    </html> """.format(header))# assiging html structure to x with a wild card for the content of <h1> use format to fill  the wild card
    f.write(x) #write the contents of variable x to the document
    f.close() # close the doc
    webbrowser.open("text.html") #open file in web browser
    

#def set_header(self):
#    header = self.filepath1.get()
#    print(header)
#    return header
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Check Files")

        self.browse_button = Button(master, text="Browse...", command = lambda: browse_button(self))
        self.browse_button.grid(row=1,column=0)

        self.browse_button = Button(master, text="set header", command = lambda: set_header(self))
        self.browse_button.grid(row=2,column=0)

        self.file_button = Button(master, text="make web page...", command = lambda: html(self))
        self.file_button.grid(row=3,column=0)

        self.filepath = folder_path
        self.filepath1 = StringVar()

        self.e1 = Entry(self.master, text=self.filepath)
        self.e1.grid(row=1,column=1)

        self.e2 = Entry(self.master, text=self.filepath1)
        self.e2.grid(row=2,column=1)
    
        self.close_button = Button(master, text="Close Program", command=master.quit)
        self.close_button.grid(row=3,column=4)



root = Tk()
folder_path = StringVar()
my_gui = MyFirstGUI(root)
root.mainloop()
