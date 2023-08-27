filename = 'PythonCrashCourse/Ch10_FilesAndExceptions/pi_digits.txt'

''' open() takes one argument: the name of the file you want to open
    Python looks for the file in the directory where the program currently being executed is stored
    open() returns an object representing the file
    keyword 'with' closes the file once access to it is no longer needed
        files can explicitly be closed with close()
'''
with open(filename) as file_object:
    ''' read() stores the entire contents of the file as one long string
        note that read() added an extra blank line at the end of the output
        this is b/c read() returns an empty string when it reaches end of file'''
    #contents = file_object.read()
    #print(contents)
    ''' alternatively, we could go through the file line by line'''
    for line in file_object:
        ''' print adds a newline each time it is called,
            so we use rstrip() to eliminate the newline characters from the file'''
        print(line.rstrip())

''' when you use 'with', you only have access to the file's contents inside the 'with' block.
    We can store the contents in a data structure to access it outside the block.'''
with open(filename) as file_object:
    ''' readlines() takes each line from the file and stores it in a list'''
    lines = file_object.readlines()
for line in lines:
    ''' replace() replaces any word in a string with a different word'''
    print(line.rstrip().replace('3', '!'))