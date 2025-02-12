from datetime import datetime

date_1 = input("Enter first date(YYYY-MM-DD): ")
date_2 = input("Enter second date(YYYY-MM-DD): ")

datedif = abs(datetime.strptime(date_2, "%Y-%m-%d") - datetime.strptime(date_1, "%Y-%m-%d")) #с помощью strptime можно строку преобразовать в дату по заданному формату 

print("Difference in seconds: ", datedif.total_seconds()) #оно преобразуит время в секунды