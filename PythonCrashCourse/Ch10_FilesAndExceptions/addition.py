prompt1 = 'First integer: '
prompt2 = 'Second integer: '
while (True):
    print("Please enter two integers or type 'q' to quit.")
    x, y = input(prompt1), input(prompt2)
    if x == 'q' or y == 'q':
        break
    try:
        res = int(x) + int(y)
    except ValueError:
        print('Error! You did not input numbers.')
    else:
        print(x + ' + ' + y + ' = ' + str(res))