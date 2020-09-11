import os

def writeData():
    data = '\nhello world'
    with open('text.txt', 'a') as f:
        f.write(data)
        print(data)
        f.close()
    

def openfile():
    with open('text.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()

if __name__ == "__main__":
    writeData()
    openfile()
