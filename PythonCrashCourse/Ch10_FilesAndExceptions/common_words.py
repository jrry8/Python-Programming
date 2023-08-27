filename = 'PythonCrashCourse/Ch10_FilesAndExceptions/Enchanted April.txt'
enc = 'utf-8'
target = 'april'
with open(filename, 'r', encoding=enc) as file_object:
    contents = file_object.read()
    numWords = len(contents.split())
    count = contents.lower().count(target)

print('The text has ' + str(numWords) + ' words.')
print(target + " appears " + str(count) + ' times in the text.')
