class User:
    num_users = 0
    def __init__(self, name):
        self.name = name
        User.num_users += 1

u = User('monkey')
print(User.num_users, u.name)
u2 = User('sunshine')
print(User.num_users, u2.name)
print(User.num_users, u.num_users, u2.num_users)
