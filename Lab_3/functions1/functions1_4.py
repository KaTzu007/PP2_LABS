def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primesFunction(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

user = input("Enter numbers separated by spaces: ")
array = list(map(int, user.split())) #мап автоматом преобразует мтринг к инт

print(primesFunction(array))