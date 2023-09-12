"""Create a regex version of Python's strip() string method
    strip([chars])
    The chars argument is a string specifying the set of characters to be removed.
    If the argument is omitted, then the function defaults to removing whitespace.
    Characters are removed from the beginning and end of the string until reaching
    a character that is not contained in the set of characters in [chars].
"""
import re

def re_strip(s: str, chars: str = None) -> str:
    if not chars:
        chars = '\\s'
    s_leading = re.compile(f"^[{chars}]*")
    s_trailing = re.compile(f"[{chars}]*$")
    stripped_leading = s_leading.sub('', s)
    stripped = s_trailing.sub('', stripped_leading)
    return stripped

tmp = '   spacious   '
print(tmp)
print(re_strip(tmp))
print('\n')
tmp = 'www.example.com'
print(tmp)
print(re_strip(tmp, 'cmowz.'))