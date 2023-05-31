import re

password = input('Please enter your password\nIt should be at least 8 characters long and can contain symbols $%#@')

pass_checker = re.compile(r'[A-Za-z0-9%$#&]{8,}\d')

print(a.group())
