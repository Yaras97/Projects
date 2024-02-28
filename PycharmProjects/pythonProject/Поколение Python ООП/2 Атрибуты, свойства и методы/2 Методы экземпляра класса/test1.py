class PiggyBank:
    def __init__(self, balance=0, volume=400):
        self.balance = balance
        self.volume = volume
    def add_coins(self, coins):
        if self.balance + coins > self.volume:
            raise ValueError('Копилка слишком мала')
        else:
            self.balance += coins
    def remove_coins(self, coins):
        if self.balance - coins < 0:
            raise ValueError('В копилке недостаточно монет')
        else:
            self.balance -= coins


user1 = User('Arthur')
user2 = User('Timur')

print(user1.friends)
print(user2.friends)

user1.add_friends(10)
user1.add_friends(20)

print(user1.friends)
print(user2.friends)