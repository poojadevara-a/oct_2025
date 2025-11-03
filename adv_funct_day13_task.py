#### CLASS TASK ########
#lambda arg:exp
# map(func,iter...)
# list_1 = [2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# list_2 = [2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# result = map(lambda a:a**2,list_1)
# print(list(result))
import itertools
list_1 = [2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
list_2 = [12,35,6,78,9,23,24,38,68,39,56,60,4,8,10]
combined_list = itertools.chain(list_1,list_2)
result = map(lambda a: a**2, combined_list )
print(list(result))

############## Coding Excercises ##################
#Task 1:
# Write a Python function square_all(numbers) that takes a list of numbers as input and 
# returns a new list containing the square of each number in the input list. 
# Use the map() function with a lambda function to implement this.
print("")
print("Task 1: New list containing the square of each number in the input list")
# Method -1:
list_1 = [12,35,6,78,9,0,23,24,38,68,39,56,60,4,8,10]
empty_list = []
for i in list_1:
    result = i**2
    empty_list.append(result)
print(empty_list)
# Method -2: using advanced function
list_1 = [12,35,6,78,9,0,23,24,38,68,39,56,60,4,8,10]
def square (a):
    return a**2
result = map(square,list_1)
print(list(result))
# Method -3: 
list_1 = [12,35,6,78,9,0,23,24,38,68,39,56,60,4,8,10]
result = map(lambda a:a**2,list_1)
print(list(result))


# Task 2:
# Write a Python function filter_positive(numbers) that takes a list of numbers as input and 
# returns a new list containing only the positive numbers from the input list. 
# Use the filter() function with a lambda function to implement this.

print("")
print("Task 2: List containing only the positive numbers from the input list")
# Method -1:
list_2 = [12,35,-6,78,9,0,-23,24,38,-68,39,56,-60,4,-8,10]
empty_list = []
for i in list_2:
    if i >= 0:
        empty_list.append(i)
print(empty_list)

# Method -2: using advanced function
list_2 = [12,35,-6,78,9,0,-23,24,38,-68,39,56,-60,4,-8,10]
def filter_positive(a):
    return a >= 0
result = filter(filter_positive, list_2)
print(list(result))

# Method -3: 
list_2 = [12,35,-6,78,9,0,-23,24,38,-68,39,56,-60,4,-8,10]
result = filter(lambda a:a>=0, list_2)
print(list(result))


# Task 3:
# Write a Python function calculate_factorial(n) that calculates the factorial of a given number n. 
# Use the reduce() function with an appropriate lambda function to implement this.
print("")
print("Task 3: Calculating the factorial of a given number")
# Method -1:
factorial = 1
n= int(input("Enter the number: "))
for i in range(1,n+1):
    factorial *= i
print(f"The factorial of {n} is - {factorial}")

# Method -2: using advanced function
n= int(input("Enter the number: "))
def calculate_factorial(a):
    if a==0 or a == 1:
        return 1
    else:
        return a * calculate_factorial(a-1)
result = calculate_factorial(n)
print(f"The factorial of {n} is - {result}")

 # Method -3: 
from functools import reduce
n= int(input("Enter the number: "))
fact_list = []
for i in range(1,n+1):
    fact_list.append(i)
print(f"The factorial of {n} is -{(reduce(lambda a,b:a *b, fact_list))}")


# Task 4:
# Write a Python function count_vowels(string) that takes a string as input and 
# returns the count of vowels (a, e, i, o, u) in the input string. 
# Use the reduce() function with an appropriate lambda function to implement this.

print("")
print("Task 4: string as input and returns the count of vowels (a, e, i, o, u)")

# Method -2: using advanced function
sentence = "Write a Python function that count_vowels"
vowels = "aAeEiIoOuU"
count = 0
def count_vowels(sentence):
    global count
    for char in sentence:
        if char in vowels:
            count += 1
    return count
print(f"Count of vowels in - {sentence} is - {count_vowels(sentence)}") 

# Method -3: 
from functools import reduce
sentence = "Write a Python function that count_vowels"
vowels = "aAeEiIoOuU"
count = 0
print(f"Count of vowels in - {sentence} is - {reduce(lambda count, char: count + (char in vowels), sentence,0)}")


























































































