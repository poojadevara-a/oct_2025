#Exercise 1:
#  Sum of Squares
# Write a Python program that calculates and prints the sum of the squares of numbers from 1 to 5 using a for loop.

sum = 0
for i in range(1,6):
    result = i**2
    sum+=result
    print(f"square of {i} is {i**2}")
print(f"The sum of squares of numbers from {i} is {sum}")



#Exercise 1(a):
#  Sum of Squares
# Write a Python program that calculates and prints the sum of the cubes of numbers from 1 to 5 using a for loop.


sum = 0
for i in range(1,6):
    result = i**3
    sum+=result
    print(f"cubes of {i} is {i**3}")
print(f"The sum cubes of the numbers from {i} is {sum}")


#Exercise 2: Countdown
# Write a Python program that uses a 
# while loop to print a countdown from 5 to 1.

count = 5
while count>=1:
    print(count)
    count -= 1


#Exercise 2(a): Countdown
# Write a Python program that uses a 
# while loop to print a countdown from 6 to 11.

count = 6
while count<=11:
    print(count)
    count += 1

#Exercise 3: Multiplication Table with Nested For Loop
#  Write a Python program to print the multiplication table for a user-specified 
# number using a nested for loop.

table = int(input("Enter the table: "))
for i in range(1,2):
    for j in range(1,11):
        print(f"{table} X {j} = {table*j}")



#Exercise 4: Write a Python program that uses a "for" loop to find the sum of all even numbers between 0 and 10 (inclusive)

sum = 0
for i in range(1,11):
    if i%2==0:
        print(i)
        sum+=i
print(f"The sum of all even numbers is {sum}")


#Exercise 5: Calculate the sum of all numbers from 1 to a given number

num = int(input("Enter the number: "))
print(num)
sum = 0
for i in range(1,num+1):
    print(i)
    sum+=i
print(f"The sum of all numbers is {sum}")



# Exercise 6: Display numbers from a list using loop

Emp_id = [2345,8970,3456,8904,7859,6474,8736,8907,6748,3589,2890]
for i in Emp_id:
    print(f"Your Employee id is {i}")


# Exercise 7:  Display numbers from -10 to -1 using for loop

for i in range(-10,0):
    print(i)


# Exercise 8:  Write a Python program to print the cube of all numbers from 1 to a given number

num = int(input("Enter the number: "))
print(num)
for i in range(1,num+1):
    result= (num)**3
print(f"The cubes of num {i} is {result}")























































































































































