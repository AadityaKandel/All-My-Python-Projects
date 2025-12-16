'''
# 1) Write a Python program that checks whether a given number is positive, negative, or zero.
number = input("Enter a number: ")
if (int(number)<0):
    print(f"{number} is a negative number")
elif (int(number)>0):
    print(f"{number} is a positive number")
elif (int(number)==0):
    print(f"{number} is a neutral number")
'''

'''
# 2) Write a Python program to find the maximum of three different numbers.
# Maximum of three numbers
# Eg: Which is the greatest of 3 numbers?
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))
if x>y>z:
    print(f"{x} is the greatest")
elif y>x>z:
    print(f"{y} is the greatest number")
else:
    print(f"{z} is the greatest number")
'''

'''
# 3) Write a Python program that checks whether a given character is a vowel or a consonant.
# Check if a given char is vowel or consonant
vowel = ['a', 'e', 'i', 'o', 'u']
char = input("Enter a single character: ")
if len(char)>1:
    print(f"Logic Error! char has more than one letter")
elif char in vowel:
    print(f"{char} is a vowel letter")
else:
    print(f"{char} is a consonant letter")
'''

'''
# 4) Write a Python program that calculates the grade based on a given percentage.
# (Example: 80-100 → A, 60-80 → B, and so on. Take percentage as input from the user.)
# Conditonal Statement for grade calculator
subjects = ['English', 'Nepali', 'Computer', 'Account', 'Social']
failed = 0
total_gained = 0
for i in range(len(subjects)):
    x = int(input(f"Enter your Marks in {subjects[i]}: "))
    if x<40:
        failed+=1
    total_gained+=x
    
percentage_gained=(total_gained/500)*100
constant = f"You've passed in all subjects with {percentage_gained}%."
if failed>0:
    print(f"You've failed in {failed} subjects")
elif (percentage_gained>=80 and percentage_gained<=100):
    print(f"{constant} You got Grade A")
elif (percentage_gained>=60 and percentage_gained<80):
    print(f"{constant} You got Grade B")
elif (percentage_gained<60):
    print(f"{constant} You got Grade C")
'''

'''
# 5) Write a Python program that determines the type of a triangle based on its side lengths (equilateral, isosceles, or scalene).
# Write a Python program that determines the type of a triangle based on its side lengths
first_side=float(input("Enter the length of the first side of a triangle: "))
second_side=float(input("Enter the length of the second side of a triangle: "))
third_side=float(input("Enter the length of the third side of a triangle: "))
if first_side==second_side==third_side:
    print("All sides are equal. Hence, its an Equilateral Triangle")
elif (first_side==second_side) or (second_side==third_side) or (first_side==third_side):
    print("Only two sides are equal. Hence, its an Isosceles Triangle")
else:
    print("None sides are equal. Its a Scalene Triangle")
'''

'''
# 6) Write a Python program that checks whether a given year (e.g., 2003, 2004) is a leap year.
# Write a Python program that checks whether a given year (e.g., 2003, 2004) is a leap year.
year = int(input("Which year do you want to calculate if it is a leap year? "))
if (year % 4==0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
'''

'''
# 7) Write a Python program that calculates the area of a shape based on user input.
# (Supported shapes: "circle", "rectangle". If the input is invalid, display "Invalid choice.")
const_PIE = 22/7
shape = input("Which shape would you like to calculate the area for? ")
if shape.lower() == "circle":
    radius = int(input("Enter the radius of the circle: "))
    area_C = const_PIE*radius*radius
    print(f"The area of circle with radius {radius} is {area_C}")
elif shape.lower() == "rectangle":
    length = int(input("Enter the length of recctangle: "))
    breadth = int(input("Enter the breadth of recctangle: "))
    area_R = length * breadth
    print(f"The area of rectangle having length {length} & breadth {breadth} is {area_R}")
else:
    print("Unsupported Shape! Please Enter a valid shape")
'''

'''
# 8) Write a Python program that takes a month as input and prints the corresponding season.
# Determine Season by Month
# Given the following month-to-season mapping:
Spring = ["March", "April", "May"]
Summer = ["June", "July", "August"]
Autumn = ["September", "October", "November"]
Winter = ["December", "January", "February"]
month = input("Enter the month? ")
if month in Spring:
    print(f"{month} is Spring Season")
elif month in Summer:
    print(f"{month} is Summer Season")
elif month in Autumn:
    print(f"{month} is Autum Season")
elif month in Winter:
    print(f"{month} is Winter Season")
else:
    print("Please Enter a Valid Month")
'''

'''
# 9) Write a Python program that converts temperature between Celsius and Fahrenheit based on user choice.
# (Prompt: "Enter 1 to convert Celsius to Fahrenheit, Enter 2 for Fahrenheit to Celsius.")
# Temperature Converter
# Convert temperature between Celsius and Fahrenheit
choice = input("Enter 1 to convert Celsius to Fahrenheit, Enter 2 for Fahrenheit to Celsius: ")
if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid choice. Please enter 1 or 2.")
'''

'''
# 10) Write a Python program that checks whether a number is divisible by 5 and 7 using if-else statements.
# Divisibility Check
# Check if a number is divisible by 5 and 7
number = int(input("Enter an integer to check divisibility: "))
if number % 5==0 and number % 7==0:
    print(f"{number} is Divisible by both 5 and 7")
elif number % 5==0:
    print(f"{number} is Divisible by 5 but not 7")
elif number % 7==0:
    print(f"{number} is Divisible by 7 but not 5")
else:
    print(f"{number} is not divisible by either 5 or 7")
'''

'''
# 11) Write a Python program that determines the winner of a Rock-Paper-Scissors game using if-else statements.
# Rock-Paper-Scissors Game Logic
# Determine the winner between User1 and User2
user1_choice = input("User 1, enter your choice (Rock, Paper, Scissors): ").lower()
user2_choice = input("User 2, enter your choice (Rock, Paper, Scissors): ").lower()
if user1_choice == user2_choice:
    print("It's a Draw!")
elif (user1_choice == 'rock' and user2_choice == 'scissors') or \
     (user1_choice == 'paper' and user2_choice == 'rock') or \
     (user1_choice == 'scissors' and user2_choice == 'paper'):
    print("User 1 Wins!")
elif (user2_choice == 'rock' and user1_choice == 'scissors') or \
     (user2_choice == 'paper' and user1_choice == 'rock') or \
     (user2_choice == 'scissors' and user1_choice == 'paper'):
    print("User 2 Wins!")
else:
    print("Invalid input. Please enter Rock, Paper, or Scissors.")
'''

'''
# 12) Number System Converter. Write a Python program that converts a given decimal number into binary, octal, or hexadecimal based on user choice.
# Number System Converter
# Convert decimal number to binary, octal, or hexadecimal
number = int(input("Enter a decimal number: "))
choice = input("Convert to (B)inary, (O)ctal, or (H)exadecimal? ").upper()
if choice == 'B':
    print(f"Binary equivalent: {bin(number)}")
elif choice == 'O':
    print(f"Octal equivalent: {oct(number)}")
elif choice == 'H':
    print(f"Hexadecimal equivalent: {hex(number)}")
else:
    print("Invalid choice. Please select B, O, or H.")
'''

'''
# 13) Character Classification. Write a Python program to check whether a given character is an alphabet, digit, or special character.
# Check if a character is an alphabet, digit, or special character
char = input("Enter a single character: ")
if len(char) != 1:
    print("Please enter exactly one character.")
elif char.isalpha():
    print(f"'{char}' is an Alphabet letter")
elif char.isdigit():
    print(f"'{char}' is a Digit")
else:
    print(f"'{char}' is a Special Character")
'''

'''
# 14) Palindrome Checker. Write a Python program that checks whether a given string is a palindrome.
# Palindrome Checker
# Check if a given string is a palindrome
text = input("Enter a string (word): ")
# Check if the reversed string is the same as the original
if text == text[::-1]:
    print(f"'{text}' is a Palindrome")
else:
    print(f"'{text}' is NOT a Palindrome")
'''

'''
# 15) Write a Python program that performs basic arithmetic operations (+, -, *, /) based on user input.
# Perform +, -, *, / based on user input
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")
'''

'''
# Nested If-Else Practice 1) Largest of Three Numbers. Write a Python program to find the largest of three numbers using nested if-else statements.
first_num = input("Enter the first number: ")
second_num = input("Enter the second number: ")
third_num = input("Enter the third number: ")

if first_num>second_num:
    if first_num>third_num:
        print(f"{first_num} is the greatest number")
elif second_num>first_num:
    if second_num>third_num:
        print(f"{second_num} is the greatest number")
elif third_num>first_num:
    if third_num>second_num:
        print(f"{third_num} is the greatest number")
'''

'''
# Nested If-Else Practice 2) Smallest of Three Numbers. Write a Python program to find the smallest of three numbers using nested if-else statements.
first_num = input("Enter the first number: ")
second_num = input("Enter the second number: ")
third_num = input("Enter the third number: ")

if first_num<second_num:
    if first_num<third_num:
        print(f"{first_num} is the smallest number")
elif second_num<first_num:
    if second_num<third_num:
        print(f"{second_num} is the smallest number")
elif third_num<first_num:
    if third_num<second_num:
        print(f"{third_num} is the smallest number")
'''

'''
# Nested If-Else Practice 3) Leap Year (Nested). Write a Python program that checks whether a given year is a leap year using nested if-else statements.
# Write a Python program that checks whether a given year (e.g., 2003, 2004) is a leap year.
year = int(input("Which year do you want to calculate if it is a leap year? "))

if (year % 4 == 0):
    if (year % 100 != 0):
        print(f"{year} is a leap year")
    elif (year % 400 == 0):
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
'''

'''
# Nested If-Else Practice 4) Write a Python program that checks whether a number is divisible by 5 and 7 using nested if-else statements.
# Divisibility Check
# Check if a number is divisible by 5 and 7
number = int(input("Enter an integer to check divisibility: "))

if number % 5 == 0:
    if number % 7 == 0:
        print(f"{number} is Divisible by both 5 and 7")
elif number % 5 == 0:
    print(f"{number} is Divisible by 5 but not 7")
elif number % 7 == 0:
    print(f"{number} is Divisible by 7 but not 5")
else:
    print(f"{number} is not divisible by either 5 or 7")
'''

'''
# Nested If-Else Practice 5) Let username =“softwarica”, password=“softwarica123” . Write a Python program that simulates a login system.
username = input("Enter the username: ")
if username == "softwarica":
    password = input("Enter the password: ")
    if password == "softwarica123":
        print("Login Successful. Welcome, Anonymous Student.")
    else:
        print("Invalid Password")
elif username != "softwarica":
    print("Invalid Username")
else:
    print("Error Occured.")
'''

'''
# Nested If-Else Practice 6) Take three integers as input, and check whether those three integers can be the three sides of a triangle or not.
first_side = int(input("Enter the first side of a triangle: "))
second_side = int(input("Enter the second side of a triangle: "))
third_side = int(input("Enter the third side of a triangle: "))

if (first_side + second_side) <= third_side or \
   (first_side + third_side) <= second_side or \
   (second_side + third_side) <= first_side:
    print(f"It is physically impossible to create a triangle with sides of length {first_side}, {second_side} and {third_side}")
else:
    if first_side == second_side:
        if second_side == third_side:
            print("It is an equilateral triangle since all sides have the same length")
        else:
            print("It is an isosceles triangle since two sides are equal to each other")
    elif second_side == third_side:
        print("It is an isosceles triangle since two sides are equal to each other")
    elif first_side == third_side:
        print("It is an isosceles triangle since two sides are equal to each other")
    else:
        print("It is a scalene triangle since none of its sides are equal")
'''
