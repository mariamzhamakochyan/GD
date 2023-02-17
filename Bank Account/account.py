class Account:
    def __init__(self):
        self.account = {}
    
    def user_(self, user, amount):
        self.account[user] = amount
    
    def getusers(self):
        return self.account
    
    def deposite(self, user, depos):
        if user not in self.account:
            print("Username has not been found")
        elif depos <= 0:
            print('Only positive input')
        else:
            self.account[user] += depos
            
    def withdrow(self, user, withd):
        if withd > self.account[user]:
            print('There is no enough money')
        elif withd <= 0:
            print('Ask about positive amount')
        elif user not in self.account:
            print("Username has not been found")
        else:
            self.account[user] -= withd
    
    def registration(self):
        user = input("Enter your name: ")
        amount = int(input("Enter the amount: "))
        a.user_(user, amount)
    
    def client(self):
        us = input("For deposite type D, and for withdrow type W...: ")
        if us == "D":
            user = input("Enter your name: ")
            amount = int(input("Enter deposite amount: "))
            a.deposite(user, amount)
        else:
            user = input("Enter your name: ")
            amount = int(input("Enter withdrow amount: "))
            a.withdrow(user, amount)
            
# a = Account()
# a.registration()
# a.client()
# print(a.getusers())
