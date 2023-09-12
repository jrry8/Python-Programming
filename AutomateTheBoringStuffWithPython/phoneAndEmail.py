# Find phone numbers and email addresses from a piece of text

import re

phone_regex = re.compile(r"""(
                        (\d{3}|\(\d{3}\))    # area code
                        (\s|\.|-)    # separator
                        (\d{3})    # first 3 digits
                        (\s|\.|-)    # separator
                        (\d{4})    # last 4 digits
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension 
                         )""", re.VERBOSE)

email_regex = re.compile(r"""(
                        [a-zA-Z0-9._%+-]+   # username
                        @
                        [a-zA-Z0-9.-]+   # domain name
                        \.[a-zA-Z]{2,4}   # dot-something
                        )""", re.VERBOSE)

filename = "AutomateTheBoringStuffWithPython/phoneAndEmail.txt"
matches = []
with open(filename) as f:
    text = f.read()
    for groups in phone_regex.findall(text):
        phone_num = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8]:
            phone_num += ' x' + groups[8]
        matches.append(phone_num)
    for email in email_regex.findall(text):
        matches.append(email)

if matches:
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
