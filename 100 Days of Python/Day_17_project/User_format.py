class Users:
    def __init__(self, user_id, username):
        print("new user has joined")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = Users("001", "alochii")
user_2 = Users("002", "megha")

user_1.follow(user_2)
print(f"{user_1.username} now has {user_1.followers} followers and follows {user_1.following} accounts")
print(f"{user_2.username} now has {user_2.followers} followers and follows {user_2.following} accounts")
