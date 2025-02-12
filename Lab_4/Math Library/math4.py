def parallelogram(length, height):
    return length * height

length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
output = parallelogram(length, height)

print(f"Expected Output: {output:.1f}")