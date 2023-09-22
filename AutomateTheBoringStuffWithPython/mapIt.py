# Launches a map in a browser using an address from the command line

import webbrowser, sys

if len(sys.argv) < 2:
    print("Missing address!")
else:
    address = ' '.join (sys.argv[1:])
    webbrowser.open('https://www.google.com/maps/place/' + address)