text = input("Enter text: ")

upper = sum(1 for char in text if char.isupper())
lower = sum(1 for char in text if char.islower())

print("Upper cases: ", upper, "; Lower cases: ", lower)