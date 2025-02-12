from math import pi

def radians(degree):
    return degree * (pi / 180)

degree = float(input("Input degree: "))
radian = radians(degree)

print(f"Output radian: {radian:.6f}")