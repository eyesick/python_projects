import os
import time
import sys
import pathlib
# Open a file
#path = "C:\\python_projects\\python assignemnt\\"
path = input("\nInput absolute path\n>>> ")
dirs = os.listdir( path )
files = [] # declare variable as a type of list with the name files 
# This store all the files and directories in the list files
for i in dirs: 
   files.append(i)
absPath = []
time_stamp = []
y = []
def makePath(y):
    for i in y: # this takes the original path and combines it with the items in the list x to create the absolute path
        absPath.append(os.path.join(path, i))
    return absPath


def getTime(absPath):    
    for i in absPath:# this gets the time stamp of last change on a file located at the abs path
        time_stamp.append(time.ctime(os.path.getmtime(i)))
    return(time_stamp)

def makeDictionary(absPath,time_stamp):
    file_timemod = {absPath[i]: time_stamp[i] for i in range(len(time_stamp))}
    print(file_timemod)
    
    
def getFileType(files):
    for i in files:
        x = pathlib.Path(i).suffix
        if x == ".txt":
            y.append(i)
    return y
    

def start():
    getFileType(files)
    makePath(y)
    getTime(absPath)
    makeDictionary(absPath,time_stamp)
    
    
start()
        
        
    


