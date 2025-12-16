'''
# Write a program that prints numbers from 1 to 10 using a while loop.
i=1
while i <=10:
    print(i)
    i+=1
'''

'''
# Print all even numbers from 2 to 20 using a while loop.
i=2
while i<=20:
    print(i)
    i+=2
'''

'''
# Ask the user to enter a number repeatedly until they enter 0, then stop.
num=-1
while num !=0:
    num = int(input("Enter a number (0 to stop): "))
print("Stopped.")
'''

'''
# Print the sum of the first 50 natural numbers using a while loop.
count = 1
sum = 0
while count <=50:
    sum += count
    count+=1
print(f"The sum of the first 50 natural numbers is {sum}")
'''

'''
# Count down from 10 to 1 using a while loop.
i=10
while i >=1:
    print(i)
    i-=1
'''

'''
# Ask the user to guess a secret number. Keep asking until they guess correctly.
secret_num = 7
guess = 0
while guess != secret_num:
    guess = int(input("Guess the secret number: "))
print("You guessed it correctly!")
'''

'''
# Take numbers from the user until they type "stop", then print the total count of numbers entered.
count = 0
while True:
    data = input("Enter a number (or type 'stop'): ")
    if data == 'stop':
        break
    count +=1
print(f"Total numbers entered: {count}")
'''

'''
# Print the factorial of a number using a while loop.
n= int(input("Enter a number to find its factorial: "))
factorial = 1
i=1
while i <= n:
    factorial = factorial * i
    i+=1
print(f"The factorial of {n} is {factorial}")
'''

'''
# Reverse a number (e.g., 12345->54321) using a while loop.
n= int(input("Enter a number to reverse: "))
rev=0
while n>0:
    digit = n % 10
    rev=rev*10+digit
    n=n//10
print(f"Reversed number: {rev}")
'''

'''
# Check if a number is a palindrome using a while loop.
n= int(input("Enter a number to check palindrome: "))
temp=n
rev=0
while temp >0:
    digit = temp% 10
    rev=rev*10+digit
    temp=temp//10
if n== rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
'''

'''
# Print the Fibonacci sequence up to N terms using a while loop.
n= int(input("Enter number of terms: "))
t1=0
t2=1
count=0
if n<=0:
    print("Please enter a positive integer")
elif n == 1:
    print(t1)
else:
    while count <n:
        print(t1)
        next_term = t1+t2
        t1=t2
        t2= next_term
        count += 1
'''

'''
# Find the largest digit in a number using a while loop.
n= int(input("Enter a number: "))
largest = 0
while n>0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n=n//10
print(f"The largest digit is {largest}")
'''

'''
# Keep asking for a password until the user enters a password that meets these rules: At least 8 characters, Contains a number.
while True:
    password = input("Enter password: ")
    has_num = False
    # Check for number
    for char in password:
        if char in '0123456789':
            has_num = True
            
    if len(password) >= 8 and has_num == True:
        print("Password accepted.")
        break
    else:
        print("Invalid password. Try again.")
'''

'''
# Create a number-guessing game where the program gives hints ("too high", "too low") until guessed.
secret = 50
guess = 0
while guess != secret:
    guess = int(input("Guess the number: "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
print("You guessed it!")
'''

'''
# 1) WAP to find the sum of first 'n' natural numbers. take 'n' as input.
n= input("Enter a number to find the sum of first natural numbers: ")
n=str(abs(int(n)))
sum=0
for i in range(1,int(n)+1):
    sum+=i
print(f"The sum of natural numbers up to {n} is {sum}")
'''

'''
# 2) WAP to take a number 'n' as input, find and display the factorial of 'n'.
n= int(input("Enter a number to find its factorial: "))
factorial = 1
for x in range(1,n+1):
    factorial = factorial*x
print(f"The factorial of {n} is {factorial}")
'''

'''
# 3) WAP to display multiplication of a number in reverse order (i.e. 5*10=50 first and 5*1=5 in last)
for mul in range(10,0,-1):
    print(f"5*{mul}={5*mul}")
'''

'''
# 4) WAP to display and count the numbers of vowels in a string entered by the user
string = input("Enter a word to count the vowel numbers: ")
vowels = 'aeiou'
count = 0
for char in vowels:
    if char in string:
        count+=1
print(f"There are {count} number of vowels in the word {string}")
'''

'''
# 5) Suppose you have a list of marks obtained by ten students as [60,67,45,87,90,78,84,38,13,56]. 
# A) Find the number of students who scored 60 or more than 60, what will be the total sum of marks obtained by only these students?
# B) is there any student who scored exactly 13?
list_of_marks = [60,67,45,87,90,78,84,38,13,56]
sum = 0
count=0

for items in list_of_marks:
    if items >=60:
        sum+=items
        count+=1
 
    if items==13:
        print("Yes. Someone has scored 13")
 
print(f"There are {count} number of students who scored greater than or equal to 60")
print(f"The sum of those students is {sum}")
'''

'''
# 6) WAP to find the sum of all the digits of a number enter by the user (23189 ==> 2+3+1+8+9 ==> 23)
digits = input("Enter a number to find the sum of its digits: ")
digit_sum=0
for num in digits:
    digit_sum+=int(num)
print(f"The sum of {digits} is {digit_sum}")
'''

'''
# 7) question: let a=[15,17,19,30,7]. find the maximum number of that list without using built in function of list.
a = [15,17,19,30,7]
initial_item = 0
for items in a:
    if items>initial_item:
        initial_item=items
print(f"The maximum number of that list is {initial_item}")
'''

'''
# 8) WAP to check whether a number enter by the user is Prime or Not
from math import *
prime_or_not = int(input("Enter the number to check if it is a prime number or not: "))
pon=True

if prime_or_not<0:
    prime_or_not = abs(prime_or_not)

for divisor in range(2,int(sqrt(prime_or_not))+1):
    if (prime_or_not % divisor ==0):
        pon=False
        break
 
if pon and (prime_or_not!=1 and prime_or_not!=0):
    print("It is a prime number")
else:
    print("It isn't a prime number")
'''

'''
# 9) WAP to take a sentence as input , display the longest word of that sentence.
sentence = input("Enter a sentence: ")
# Split the sentence into words
words = sentence.split()
max_len = 0
 
for items in words:
    if len(items) > max_len:
        max_len = len(items)
 
for items in words:
    if max_len == len(items):
        print(items)
'''

'''
# 10) WAP to generate Fibonacci series up to n terms
first_term = 0
second_term = 1
nth = int(input("Enter the number to find its fibonacci series: "))
 
if (nth>=0):print("0")
if (nth>=1):print("1")
 
for x in range(1,nth):
    third_temp = first_term+second_term
    first_term=second_term
    second_term=third_temp
    print(second_term)
'''

'''
# 11) WAP to check whether a number entered by the user is Armstrong or not.
number = input("Enter a integer to find if it is an armstrong or not: ")
 
# Properly removes the floating value with assumption that user doesn't provide the floating value and value less than 0
number = str(abs(int(float(number))))
 
power = len(number) 
superscripts = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
 
symbol=""
for char in str(power):
    symbol+=superscripts[int(char)]
 
calculated_sum = 0
process_display = ""
for char in number:
    calculated_sum += int(char)**power
    process_display +=f"{char}{symbol}+"
 
if calculated_sum == int(number):
    print(f"It is an armstrong number because {process_display[0:-1]}={calculated_sum}={number}")
else:
    print(f"It is not an armstrong number because {process_display[0:-1]}={calculated_sum}!={number}")
'''
