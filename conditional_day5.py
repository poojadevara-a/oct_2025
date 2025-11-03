#Excercise_1 : Vowel Checker: 
# Write a Python program that takes a character as input and checks whether it is a vowel or not. 
# Use the if-else statement.

#enter the character from a to z
char_input = input("Enter the charater of your choice: ")

if char_input in "aeiou" or char_input in "AEIOU":
    print(f"Given character {char_input}, is in vowel")
else:
    print(f"Given charater {char_input}, is a consonant")



#Excercise_2 : Age Group Classification
#  Write a program that takes an age as input and classifies the person into one of the following age groups:
#  Child: 012 years
# Teenager: 1317 years
# Adult: 1864 years
# Senior: 65 years and older

Age = int(input("Enter your age: "))

if Age < 0:
    print(f"Invalid age. Age should not be less than 0")
elif Age <= 12:
    print(f"You are a child as your age is {Age}")
elif Age <= 17:
    print(f"You are a teenager as your age is {Age}")
elif Age <= 64:
    print(f"You are an adult as your age is {Age}") 
else:
    print("you are a senior citizen")


#approach by sir

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age <= 12:
    print("You are a Child.")
elif age <= 17:
    print("You are a Teenager.")
elif age <= 64:
    print("You are an Adult.")
else:
    print("You are a Senior.")



#Excercise_3 : Number Classifier:
# Write a program that takes an integer as input and classifies it as positive, negative, or zero. 
# Use the if-elif-else statement.

Num = int(input("Enter the number: "))

if Num > 0:
    print(f"The given number {Num}, is positive number")
elif Num < 0:
    print(f"The given number {Num}, is negative number")
else:
    print(f"The given number is Zero")



#Excercise_4 : Leap Year Checker:
#  Create a program that checks whether a given year is a leap year or not. 
# A leap year is divisible by 4, but not by 100 unless it is divisible by 400.


year = int(input("Enter the year: "))

if year%4 ==0 or year%400 ==0:
    print(f"The given year {year}, is a Leap year.")
else:
    print(f"The given year {year}, is not a leap year")



#Excercise_5 : Calculator:
# Build a simple calculator program that takes two numbers and an operator (+, -, *, /) as input 
# and performs the corresponding operation.

num1 = int(input("Enter the number_1: "))
num2 = int(input("Enter the number_2: "))
#taken operators (+, -, *, /) only for this code
operator = input("""Enter the "+" for addition
                 Enter the "-" for subtraction
                 Enter the "*" for multiplication
                 Enter the "/" for division 
                 Enter your operator: """)

if operator == "+":
    print(f"The operation between the numbers {num1} and {num2} using the operator {operator}, gives the result is {num1 + num2}")
elif operator == "-":
    print(f"The operation between the numbers {num1} and {num2} using the operator {operator}, gives the result is {num1 - num2}")
elif operator == "*":
    print(f"The operation between the numbers {num1} and {num2} using the operator {operator}, gives the result is {num1 * num2}")
elif operator == "/":
    print(f"The operation between the numbers {num1} and {num2} using the operator {operator}, gives the result is {num1 / num2}")
else:
    print("The given operator is invalid")



#Excercise_6 : Short Hand If:
# Rewrite the following code using the short-hand 
# if statement:
# x = 8
# if x % 2 == 0: result = "Even"
# else: result = "Odd"

x = 8
print(f"x is even") if x % 2 == 0 else print(f"x is odd")



#Excercise_7 : Discount Calculator:
# Create a program that calculates the final price after applying a discount. 
# The program should take the original price and the discount percentage as input.
#Discounted price = Original price - (Original price x Discount (%) / 100)

org_pri = float(input("Enter the price of the product: "))
dis_per = int(input("Enter the discount percentage:  "))
dis_price = (org_pri * dis_per/100)
print(dis_price)
final_price = org_pri - dis_price
print(final_price)

print(f"Original price of the product is {org_pri}/., discounted percentage is {dis_per}% and the dicounted price of the product after the dicount is {final_price}/.")



#Excercise_8 :  BMI Calculator:
# Write a program that calculates the Body Mass Index BMI using the 
# formula: BMI = weight (kg) / (height (m))^2. 
# The program should take weight and height as input.
#bmi = weight / (height ** 2)

weight = float(input("Enter your weight in Kgs.: "))
height = float(input("Enter your height in meters: "))

print(f"If the weight is {weight}Kgs. and the height is {height}m, then the BMI of the person {weight / (height** 2)}")

 




























































































































