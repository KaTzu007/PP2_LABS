def decreasing(num):
    for i in range(num, -1, -1):
        yield i

n = int(input())
for i in decreasing(n):
    print(i)