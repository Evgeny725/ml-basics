# git remote add origin https://github.com/Evgeny725/ml-01.git
# git branch -M main
# git push -u origin main
import string
from decimal import Decimal

print("hello world")

x = 1 + 1
print(x)


a = Decimal('0.56')
print(a)

# use example below to declare infinite value
b = float('inf')
print(b)

# to represent a number as hex value and vice versa

hex(123456)
print(hex(123456))

d = int('1e240',16)
print(d)

# truncate string <strip>, from right end <rstrip>, from left end <lstrip>
str1 = '  abcdef     '
str2 = str1.strip(' ')
print(str2)

# string
name = 'abc'
age = 123
string = f'name is {name} and age is {age}'
print(string)

# cascade call
str3 = '  ABC DEF GHI '
str4 = str3.strip(' ').lower().split()
print(str4)

# if else
# leap year check

def leap_year():

    print('enter year (e.g. 2025)')
    year = int(input())

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap = True
        print('leap year')

    else:
        leap = False
        print('not leap year')
    return leap

# leap_year()


# mre examples
number = 1
result = 'even' if number % 2 == 0 else 'odd'
print(result)


# while, for

