import vk

APP_ID = 5647629


def get_user_login():
    return input("Enter login: ")


def get_user_password():
    return input("Enter password: ")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    online = api.friends.getOnline()
    return api.users.get(user_ids=online)


def output_friends_to_console(friends_online):
    print("\nYour online friends are:\n")
    for user in friends_online:
        print(user["first_name"], user["last_name"])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
