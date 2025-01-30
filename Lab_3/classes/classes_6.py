class PrimeList:
    def __init__(self, numbers):
        self.numbers = numbers

    def getPrimes(self):
        return list(filter(lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)), self.numbers)) #all возвращает False, если хотя бы один элемент не соответствует условию.

numbers = []
num = int(input("Size of list: "))
for i in range(0, num):
    element = int(input())
    numbers.append(element)

plist = PrimeList(numbers)
print(plist.getPrimes())
