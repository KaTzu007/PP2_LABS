def evens(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            yield i

num = int(input())
print(", ".join(map(str, evens(0, num))))