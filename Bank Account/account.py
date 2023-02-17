class Account:
    def __init__(self):
        self.account = {}
    
    def user_(self, user, amount):
        self.account[user] = amount
    
    def getusers(self):
        return self.account
    
    def deposite(self, user, depos):
        if depos > 0:
            self.account[user] += depos
        else:
            return 'Only positive input'

    def withdrow(self, user, withd):
        if withd > self.account[user]:
            return 'There is no enough money'
        elif withd <= 0:
            return 'Ask about positive amount'
        else:
            self.account[user] -= withd
