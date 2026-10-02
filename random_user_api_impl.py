from randomuser import RandomUser
import pandas as pd

r = RandomUser()
some_users = r.generate_users(10)

for user in some_users:
    print(user.get_full_name())

for user in some_users:
    print(user.get_picture())

def get_users():
    users = []

    for user in some_users:
        users.append({
            'full_name': user.get_full_name(),
            'picture': user.get_picture()
        })

    return pd.DataFrame(users)

print(get_users())