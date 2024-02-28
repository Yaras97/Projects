class User:
    def __init__(self, name, friends=0):
        self.name = name
        self.friends = friends

    def add_friends(self, n):
        self.friends += n

user = User('Arthur')

user.add_friends(0)
user.add_friends(1)
user.add_friends(2)
user.add_friends(0)
user.add_friends(1)
user.add_friends(2)

print(user.friends)