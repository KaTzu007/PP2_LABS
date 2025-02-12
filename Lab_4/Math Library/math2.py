def trapezoid(h, a, b):
    return (a + b) / 2 * h

h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))

print(f"Expected Output: {trapezoid(h, a, b)}")