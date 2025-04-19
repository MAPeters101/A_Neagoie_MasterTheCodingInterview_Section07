class User:
    age = 54
    name = 'Kylie'
    magic = True
    def __init__(self):
        pass

    def scream(self):
        print('ahhhhhh!')

user1 = User()
print(user1.age)
user1.spell = 'abra kadabra'
print(user1.spell)
user1.scream()



