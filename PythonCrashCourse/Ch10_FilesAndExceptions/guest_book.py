prompt = "(Enter 'quit' to end the program)\nPlease enter your name: "
filename = 'PythonCrashCourse/Ch10_FilesAndExceptions/guest_book.txt'

with open(filename, 'a') as file_object:
    while (True):
        name = input(prompt)
        if name == 'quit':
            break
        file_object.write(name.title() + '\n')
        print('Welcome ' + name.title() + '!')

