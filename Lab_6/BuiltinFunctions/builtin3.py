text = input("Enter text: ")

if text.lower().replace(" ", "") == text[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome")