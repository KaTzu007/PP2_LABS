from functions1_2 import fahrenheitToCelcium
from functions1_1 import gramsToOunces
from functions1_6 import reverseWords

fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
print("Fahrenheit to celcium: ", fahrenheitToCelcium(fahrenheit))

grams = int(input("Enter gram: "))
print("Gram to ounces: ", gramsToOunces(grams))

sentence = input("Enter a sentence: ")
print("Reversed order: ", reverseWords(sentence))