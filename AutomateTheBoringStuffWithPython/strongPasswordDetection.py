"""A strong password is defined as:
    at least 8 characters long
    contains both uppercase and lowercase characters
    has at least one digit
"""
import re

password = input("Password: ")
check_len = re.compile(r".{8,}").search(password)
check_upper = re.compile(r"[A-Z]").search(password)
check_lower = re.compile(r"[a-z]").search(password)
check_digit = re.compile(r"\d").search(password)
if (check_len and check_upper and check_lower and check_digit):
    print("That's a strong password!")
else:
    print("Your password is not strong enough!")