import vk
import getpass


APP_ID = 6462270


def get_user_login():
    return input('Pass your login\\number here:\n')


def get_user_password():
    return getpass.getpass()


def get_session(login, password, v_api='5.3.5'):
    session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='users, friends',
            )
    return vk.API(session, v=v_api)


def get_online_friend_ids(session):
    return session.friends.getOnline()


def get_friends_names(session, online_friend_ids):
    return session.users.get(
        user_ids=online_friend_ids,
        fields='first_name, last_name')


def output_friends_to_console(friends_online):
    print('Friends online:')
    for friend in friends_online:
        first_name = friend['first_name']
        last_name = friend['last_name']
        print(first_name, last_name)


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        session = get_session(login, password)
    except vk.exceptions.VkAuthError:
        exit('Incorrect login\password')
    friends_online = get_online_friend_ids(session)
    online_friends_names = get_friends_names(session, friends_online)
    output_friends_to_console(online_friends_names)
