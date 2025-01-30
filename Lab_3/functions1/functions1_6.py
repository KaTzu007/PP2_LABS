def reverseWords(text):
    words = text.split()
    rsentence = ' '.join(reversed(words))
    return rsentence

text = input("Enter text: ")
print(reverseWords(text))