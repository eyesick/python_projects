import datetime
from pytz import timezone    

south_africa = timezone('Africa/Johannesburg')
sa_time = datetime.now(south_africa)
print (sa_time.strftime('%Y-%m-%d_%H-%M-%S'))
current_time = datetime.datetime.now()
print(current_time)
