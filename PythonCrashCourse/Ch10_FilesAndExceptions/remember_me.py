import json

filename = 'PythonCrashCourse/Ch10_FilesAndExceptions/username.json'

def get_stored_username():
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
            return username
    except FileNotFoundError:
        return None

def get_new_username():
    username = input('What is your name? ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print('Are you user ' + username + '? [Y/N]')
        if input().lower() == 'y':
            print('Welcome back ' + username + '!') 
            return
    username = get_new_username()
    print("We'll remember you when you come back, " + username + '!')

greet_user()