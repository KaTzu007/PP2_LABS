def divisible34(num):
    for i in range(0, num + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n  = int(input())
for i in divisible34(n):
    print(i)