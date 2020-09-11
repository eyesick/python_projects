import os

fName = "hello.txt"

fPath = 'C:\\a\\'

abPath = os.path.join(fPath, fName)

print(abPath)
