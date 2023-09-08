from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")

print('Opening the file...')
f = open(filename, 'w')

print("Now I'm going to ask you for three lines.")
line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

print("I'm going to write these to the file.")

content = "{}\n{}\n{}"
f.write(content.format(line1, line2, line3))

print("And finally, we close it.")
f.close()