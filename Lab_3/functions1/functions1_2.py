def fahrenheitToCelcium(F):
    return (5 / 9) * (F - 32)

temperature = float(input("Enter Fahrenheit: "))
print("Fahrenheit to celcium: ", fahrenheitToCelcium(temperature))