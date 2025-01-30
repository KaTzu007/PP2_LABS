from random import randint

def guessTheNumber(guess, user):
    guesses = 1
    randomInt = randint(1, 20)
    print()

    while guess != randomInt:
        if guess > randomInt:
            print('''Your guess is too high.
Take a guess.''')
            guess = int(input())
            guesses += 1
            
        else:
            print('''Your guess is too low.
Take a guess.''')
            guess = int(input())
            guesses += 1

    print(f"Good job, {user}! You guessed my number in {guesses} guesses!")

print("Hello! What is your name?")
user = input()

print(f'''Well, {user}, I am thinking of a number between 1 and 20.
Take a guess.''')

guess = int(input())

guessTheNumber(guess, user)