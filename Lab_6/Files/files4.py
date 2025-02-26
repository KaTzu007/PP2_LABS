file = open("files4.txt")

count = 0
for lines in file:
    count += 1

print("Number of lines: ", count)

file.close()