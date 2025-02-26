file = open("files5.txt", "w")

size = int(input("List's size: "))
list = []

for i in range(0, size):
    element = int(input())
    list.append(element)

file.write(str(list))
file.close()



file = open("files5.txt", "r")

print(file.read())
file.close