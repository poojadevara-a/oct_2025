# Task 1: Add Function
#  Write a Python function named add that takes two arguments a and b and returns their sum.
print("Task 1: Add Function")
def add(num1,num2):
    print(num1 + num2)
add(20,30)


# Task 2: Square Function
#  Write a Python function named square that takes a number x as input and returns its square.

print(" ")
print("Task 2: Square Function")
num = int(input("Enter the number: "))
def squr (num):
    print(num**2)
squr(num)


# Task 3: Factorial Function
# Write a Python function named factorial that takes a positive integer n as input and returns its factorial.
print(" ")
print("Task 3: Factorial Function")
def factorial(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return "Factorial can not be defined for negative numbers"
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result
    
print(factorial(5))   
print(factorial(0))   
print(factorial(-10))



# Task 4: Maximum Function
# Write a Python function named maximum  that takes a list of numbers as input and returns the maximum value in the list.
print(" ")
print("Task 4: Maximum Function")
list_4 = [23,45,12,41,7,58,23,69,456,52,2,8,4,78,21]
print(max(list_4))


#  Task 5: Reverse Function
# Write a Python function named reverse  that takes a string s  as input and returns its reverse.
print(" ")
print("Task 5: Reverse Function")
s = str(input("Enter a word: "))
print(s[::-1])


# Task 6: Check Prime Function
# Write a Python function named is_prime that takes a positive integer n as input and returns True if n is  prime, otherwise False.
print(" ")
print("Task 6: Check Prime Function")
n = int(input("Enter the number: "))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i== 0:
            return False
    else:
        return True
print(is_prime(n))

    

# Task 7: Fibonacci Function
# Write a Python function named fibonacci that takes a positive integer n as input and returns the nth Fibonacci number.
print(" ")
print("Task 7: Fibonacci Function")
n = int(input("Enter the number: "))
def fibernocci(n):
    a = 0
    b = 1
    if n < 0:
        return "Invalid input."
    if n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1,n):
            c = a+b
            a = b
            b = c
        return b
print(f"Fibernocci number for {n} is {fibernocci(n)}")


#  Task 8: Palindrome Function
# Write a Python function named is_palindrome that takes a string s as input and 
# returns True if s is a palindrome, otherwise False
print(" ")
print("Task 8: Palindrome Function")
my_string = input("Enter the string: ").lower()
def palindrome(string_8):
    if my_string == my_string[::-1]:
        return True
    else:
        return False
print(f"{my_string} is a palindrome - {palindrome(my_string)}")


# Task 9: Sum of Squares Function
# Write a Python function named  sum_of_squares that takes a list of numbers as input and 
# returns the sum of the squares of those numbers.
print(" ")
print("Task 9: Sum of Squares Function")
my_list = [12,3,5,71,15,9,14,25]
sum=0
def sum_of_squares(my_list):
    sum=0
    for i in my_list:
        sum += (i**2)
    return sum
print(sum_of_squares(my_list))


#  Task 10: Average Function
# Write a Python function named average that takes a list of numbers as input and
# returns the average value.
print(" ")
print("Task 10: Average Function")
my_list = [12,18,17,3,5,6,7,10]
def average(my_list):
    sum = 0
    result = 0
    len_my_list = len(my_list)    
    for i in my_list:
        sum += i
    result = (sum/len_my_list)
    return result
print(average(my_list))

































































































































































