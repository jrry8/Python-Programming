import json

filename = 'PythonCrashCourse/Ch10_FilesAndExceptions/favorite_number.json'
try:
    with open(filename) as f_obj:
        favNum = json.load(f_obj)
        print('Your favorite number is ' + favNum + '!')
except FileNotFoundError:
    favNum = input("What is your favorite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(favNum, f_obj)
