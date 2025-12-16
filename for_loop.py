'''
# Find sum of first n natural numbers
n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)
'''

'''
# Find factorial of a number
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)
'''

'''
# Display multiplication of 5 in reverse order
for i in range(10, 0, -1):
    print(f"5 * {i} = {5*i}")
'''

'''
# Count vowels in a string
string = input("Enter a word: ")
vowels = "aeiou"
count = 0

for char in vowels:
    if char in string:
        count += 1

print(count)
'''

'''
# Find maximum number in a list without using built-in functions
a = [15, 17, 19, 30, 7]
max_num = 0

for item in a:
    if item > max_num:
        max_num = item

print(max_num)
'''

'''
# Check whether a number is prime
from math import sqrt

num = int(input("Enter a number: "))
is_prime = True

if num < 0:
    num = abs(num)

for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num not in (0, 1):
    print("Prime")
else:
    print("Not Prime")
'''
