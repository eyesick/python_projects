import shutil
import os
import sys
import time
import datetime
from datetime import timedelta
from datetime import datetime


source = '\\Users\\isaac\\Desktop\\a\\'

destination ='\\Users\\isaac\\Desktop\\b\\'
files = os.listdir(source)


for i in files:
    # Get last modified date and today's date
    modifyDate = datetime.fromtimestamp(os.path.getmtime(source+i))
    todaysDate = datetime.today()
    
    
    # If modified within last 24 hours, then copy to destination folder
    modifyDateLimit = modifyDate + timedelta(hours=24)

    print(modifyDate,todaysDate,modifyDateLimit)
    if modifyDateLimit > todaysDate:
         shutil.copy2(source+i, destination)
#for i in files:
#    time = datetime.fromtimestamp(os.path.getmtime(source+i))
#    print(time)

# for i in files:
#    shutil.move(source+i, destination)

