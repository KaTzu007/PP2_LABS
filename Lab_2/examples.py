#Boolean;
# Example 1
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

#Example 2
# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

#Example 3
# print(bool("Hello"))
# print(bool(15))

#Example 4
# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))

#Example 5
# bool("abc")
# bool(123)
# bool(["apple", "cherry", "banana"])

#Example 6
# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})

#Example 7
# class myclass():
#   def __len__(self):
#     return 0

# myobj = myclass()
# print(bool(myobj))

#Example 8
# def myFunction() :
#   return True

# print(myFunction())

#Examplr 9
# def myFunction() :
#   return True

# if myFunction():
#   print("YES!")
# else:
#   print("NO!")

#Example 10
# x = 200
# print(isinstance(x, int))





#Operators
#Example 11
# print(10 + 5)

#Example 12
# print((6 + 3) - (6 + 3))

#Example 13
# print(100 + 5 * 3)

#Example 14
# print(5 + 4 - 7 + 3)





#List
#Example 15
# thislist = ["apple", "banana", "cherry"]
# print(thislist)

#Example 16
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

#Example 17
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

#Example 18
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

#Example 19
# list1 = ["abc", 34, True, 40, "male"]

#Example 20
# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

#Example 21
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

#Example 22
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

#Example 23
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

#Example 24
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

#Example 25
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

#Example 26
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

#Example 27
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

#Example 28
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

#Example 29
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

#Example 30
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

#Example 31
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

#Example 32
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

#Example 33
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

#Example 34
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

#Example 35
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

#Example 36
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

#Example 37
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

#Example 38
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

#Example 39
# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

#Example 40
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

#Example 41
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

#Example 42
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

#Example 43
# thislist = ["apple", "banana", "cherry"]
# del thislist

#Example 44
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

#Example 45
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

#Example 46
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

#Example 47
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

#Example 48
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

#Example 49
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

#Example 50
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

#Example 51
# newlist = [x for x in fruits if x != "apple"]

#Example 52
# newlist = [x for x in range(10)]

#Example 53
# newlist = [x for x in range(10) if x < 5]

#Example 54
# newlist = [x.upper() for x in fruits]

#Example 55
# newlist = [x.upper() for x in fruits]

#Example 56
# newlist = [x if x != "banana" else "orange" for x in fruits]

#Example 57
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

#Example 58
# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

#Example 59
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

#Example 60
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)

#Example 61
# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

#Example 62
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

#Example 63
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

#Example 64
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

#Example 65
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

#Example 66
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

#Example 67
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)

#Example 68
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

#Example 69
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

#Example 70
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)





#Tuples
#Example 71
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

#Example 72
# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

#Example 73
# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

#Example 74
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)

#Example 75
# tuple1 = ("abc", 34, True, 40, "male")

#Example 76
# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

#Example 77
# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

#Example 78
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

#Example 79
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

#Example 80
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

#Example 81
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

#Example 82
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])

#Example 83
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

#Example 84
# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")

#Example 85
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

#Example 86
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

#Example 87
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

#Example 88
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)

#Example 89
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

#Example 90
# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

#Example 91
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

#Example 92
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

#Example 93
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)

#Example 94
# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])

#Example 95
# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

#Example 96
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

#Example 97
# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)





#Sets
#Example 98
# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)

#Example 99
# thisset = {"apple", "banana", "cherry", False, True, 0}
# print(thisset)

#Example 100
# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))

#Example 101
# myset = {"apple", "banana", "cherry"}
# print(type(myset))

#Example 102
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

#Example 103
# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

#Example 104
# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)

#Example 105
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

#Example 106
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)

#Example 107
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)

#Example 108
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

#Example 109
# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)

#Example 110
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop() #random element
# print(x)
# print(thisset)

#Example 111
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

#Example 112
# thisset = {"apple", "banana", "cherry"}
# del thisset #Completely delete the set
# print(thisset)

#Example 113
# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

#Example 114
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)

#Example 115
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1 | set2
# print(set3)

#Example 116
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1.union(set2, set3, set4)
# print(myset)

#Example 117
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1 | set2 | set3 |set4
# print(myset)

#Example 118
# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)
# print(z)

#Example 119
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(set1)

#Example 120
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2) #return intersection
# print(set3)

#Example 121
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 & set2 #instead of intersection
# print(set3)

#Example 122
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)

# print(set1)

#Example 123
# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)

# print(set3)

#Example 124
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)

# print(set3)

#Example 125
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 - set2
# print(set3)

#Example 126
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.difference_update(set2)

# print(set1)

#Example 127
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.symmetric_difference(set2) #like outer join

# print(set3)

#Example 128
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 ^ set2
# print(set3)

#Example 129
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.symmetric_difference_update(set2)

# print(set1)





#Dictionary
#Example 130
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

#Example 131
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

#Example 132
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))

#Example 133
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

#Example 134
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("model")
# y = thisdict.keys()


#Example 135
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.keys()
# print(x) #before the change
# car["color"] = "white"
# print(x) #after the change

#Example 136
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.values()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change

#Example 137
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.items()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change

#Example 138
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Example 139
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})

#Example 140
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

#Example 141
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})

#Example 142
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

#Example 143
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

#Example 144
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)

#Example 145
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

#Example 146
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)

#Example 147
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(x)

#Example 148
# for x in thisdict:
#   print(thisdict[x])

#Example 149
# for x in thisdict.values():
#   print(x)

#Example 150
# for x in thisdict.keys():
#   print(x)

#Example 151
# for x, y in thisdict.items():
#   print(x, y)

#Example 152
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

#Example 153
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)

#Example 154
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

#Example 155
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

#Example 156
# print(myfamily["child2"]["name"])

#Example 157
# for x, obj in myfamily.items():
#   print(x)

#   for y in obj:
#     print(y + ':', obj[y])





#If... else
#Example 158
# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")

#Example 159
# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")

#Example 160
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

#Example 161
# a = 2
# b = 330
# print("A") if a > b else print("B")

#Example 162
# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

#Example 163
# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")

#Example 164
# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")

#Example 165
# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")

#Example 166
# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")

#Example 167
# a = 33
# b = 200

# if b > a:
#   pass





#While Loop
#Example 168
# i = 1
# while i < 6:
#   print(i)
#   i += 1

#Example 169
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

#Example 170
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

#Example 171
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")





#For Loop
#Example 172
# for x in "banana":
#   print(x)

#Example 173
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

#Example 174
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

#Example 175
# for x in range(6):
#   print(x)

#Example 176
# for x in range(2, 6):
#   print(x)

#Example 177
# for x in range(2, 30, 3):
#   print(x)

#Example 178
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

#Example 179
# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!") #does not print

#Example 180
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

#Example 181
# for x in [0, 1, 2]:
#   pass