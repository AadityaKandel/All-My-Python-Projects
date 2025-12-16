'''
# Print numbers from 1 to 10 using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1
'''

'''
# Print all even numbers from 2 to 20
i = 2
while i <= 20:
    print(i)
    i += 2
'''

'''
# Print multiplication table from 1 to 4
number = 1
index = 1

while True:
    if index > 10:
        index = 1
        number += 1
        print()

    if number > 4:
        break

    print(f"{number}*{index}={number*index}")
    index += 1
'''

'''
# Print a 3x3 star square
count = 0
star_square = ""

while count < 3:
    length = 0
    while length < 3:
        star_square += "*"
        length += 1
    star_square += "\n"
    count += 1

print(star_square)
'''

'''
# Reverse a number using while loop
n = int(input("Enter a number to reverse: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(rev)
'''

'''
# Find the largest digit in a number
n = int(input("Enter a number: "))
largest = 0

while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n = n // 10

print(largest)
'''
