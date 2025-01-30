def uniqueList(list):
    result = []

    for i in list:
        if i not in result:
            result.append(i)
    
    return result

size = int(input("Enter size of your list: "))
list = []

for i in range(0, size):
    num = int(input())
    list.append(num)

print(uniqueList(list))