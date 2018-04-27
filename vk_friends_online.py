import vk
import getpass
from time import sleep
from sys import exit


APP_ID = 6462270


def get_user_login():
    return input('Pass your login\\number here:\n')


def get_user_password():
    return getpass.getpass()


def get_session(login, password):
    session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='users, friends',
            )
    return vk.API(session, v='5.3.5')


def get_online_friends(session):
    return session.friends.getOnline()


def get_name(session, user_id):
    return session.users.get(user_id=user_id, fields='first_name, last_name')


def output_friends_to_console(friends_online):
    sleep_time = 0.3
    print('Friends online:')
    for friend in friends_online:
        user_info = get_name(session, friend)
        first_name = user_info[0]['first_name']
        last_name = user_info[0]['last_name']
        print(first_name, last_name)
        sleep(sleep_time)


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        session = get_session(login, password)
    except vk.exceptions.VkAuthError:
        exit('Incorrect login\password')
    friends_online = get_online_friends(session)
    output_friends_to_console(friends_online)
