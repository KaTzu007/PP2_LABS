def calcVolume(radius):
    return 4 / 3 * 3.14 * radius**3

radius = int(input("Radius: "))
print(calcVolume(radius))