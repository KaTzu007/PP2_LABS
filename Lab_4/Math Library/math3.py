from math import pi, tan

def polygon(sides, length):
    return (sides * length**2) / 4 * tan(pi/sides)

sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))

print(f"The area of the polygon is: {round(polygon(sides, length))}")