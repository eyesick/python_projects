import shutil
import os

source = '\\Users\\isaac\\Desktop\\a'

destination ='\\Users\\isaac\\Desktop\\b'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
