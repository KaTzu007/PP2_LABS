class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def getInfo(self):
        print(f"Owner name: {self.owner}, and balance: {self.balance}")

    def deposit(self, money):
        self.balance += money
        return self.balance
    
    def withdraw(self, money):
        if money <= self.balance:
            self.balance = self.balance - money
            return self.balance
        else:
            print(f"{self.owner} can not withdraw {money}, because {money} is much more than owner's balance({self.balance})")
    
owner1 = Account("Azamat")
owner2 = Account("Ilon Mask", 9999999990)
owner3 = Account("Student", 47135)

owner1.getInfo()
owner2.getInfo()
owner3.getInfo()

print("Balance after deposit: ", owner1.deposit(10000))

owner3.withdraw(50000)
owner2.withdraw(1000000)
owner2.getInfo()