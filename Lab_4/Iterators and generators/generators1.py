def square(start, end):
    for i in range(start, end + 1):
        yield i**2

num = int(input())
for i in square(1, num):
    print(i)