original = open("original7.txt")
copy = open("copy7.txt", "w")

for line in original:
    copy.write(line)

original.close()
copy.close()