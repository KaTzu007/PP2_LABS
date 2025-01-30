def checkPalindrome(word):
    word = word.lower()
    rword = word[::-1]
    
    if rword == word:
        return True
    return False
    
word = input("Enter a word: ")

if checkPalindrome(word):
    print("Palindrome")

else:
    print("Not palindrome")