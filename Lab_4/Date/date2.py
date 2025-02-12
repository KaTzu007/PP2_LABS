from datetime import datetime, timedelta

date = datetime.now()
yesterday = date - timedelta(1)
tommorow = date + timedelta(1)

print("Yesterday is ", yesterday.strftime("%Y.%m.%d"))
print("Today is ", date.strftime("%Y.%m.%d"))
print("Tommorow is ", tommorow.strftime("%Y.%m.%d"))