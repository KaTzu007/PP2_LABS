text = input("Enter text: ")

text = text.lower().replace(" ", "")

if text == text[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome")