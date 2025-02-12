from datetime import datetime, timedelta

date = datetime.now()
subsdate = date - timedelta(5) #timedeta просто хранит в себе время

print(subsdate.strftime("%Y.%m.%d")) #таким образом можно отформатировать дату в строку