class BankAccount:
    def __init__(self, owner, card_number, balance):
        self.owner = owner
        self.card_number = card_number
        self.is_active = True
        self.balance = balance

    def deposit(self, amount):
        if self.is_active==False:
                raise ValueError('your accont isnt active')
        elif amount<=0:
                raise ValueError('value cant be zero')
        self.balance += amount

    def withdraw(self, amount):
        if self.is_active==False:
                raise ValueError('your accont isnt active')
        elif amount<=0:
                raise ValueError('value cant be zero')            
        self.balance -= amount

    def transfer(self, maghsad, amount):
        if self.is_active==False or maghsad.is_active==False:
                raise ValueError('your accont isnt active')
        elif amount<=0:
                raise ValueError('value cant be zero')              
        self.withdraw(amount)
        maghsad.deposit(amount)