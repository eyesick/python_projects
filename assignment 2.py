import sqlite3
import pathlib
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'world.txt','data.pdf','myphoto.jpg')
y = []
msg = []
def create_table():
    conn = sqlite3.connect('test1.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileName TEXT)")
        conn.commit()
    conn.close()

def getFileType(fileList):
    for i in fileList:
        x = pathlib.Path(i).suffix
        if x == ".txt":
            y.append(i)
    return y

def appendDB(y):
    conn = sqlite3.connect('test1.db')
    with conn:
        cur = conn.cursor()
        for i in y:
            cur.execute("INSERT INTO tbl_persons(col_fileName) VALUES (?)", \
                (i,))
    conn.close()

def query():
    conn = sqlite3.connect('test1.db')
    with conn:
        cur = conn.cursor()
        cur.execute("Select * FROM tbl_persons")
        varfile = cur.fetchall()
        for i in varfile:
            msg.append(i)
        print(msg)


def start():
    create_table()
    getFileType(fileList)
    appendDB(y)
    query()
start()
