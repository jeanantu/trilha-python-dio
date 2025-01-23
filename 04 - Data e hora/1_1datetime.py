import datetime

d = datetime.date(2025,4,3)
print(d)


### outra forma importar classe
from datetime import date, datetime, time, timedelta
tempo_pequeno = 30

print (date(2024,5,28))
print (datetime.today())
print (datetime.now())
print (datetime.now() -  timedelta(minutes=60))

