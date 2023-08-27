filename = 'PythonCrashCourse/Ch10_FilesAndExceptions/programming.txt'

''' if second argument is not provided for open(), it will default to read-only
    open modes: read (r), write (w), append (a)
    if you open an existing file in write-mode, you will overwrite it.
    use append mode to add to an existing file'''
with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')

''' if we used 'w' instead of 'a' for open() here, 
    the previous two lines would have been overwritten'''
with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')