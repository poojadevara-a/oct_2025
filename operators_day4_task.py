##################### Operators Task #########################

#Exercise 1: Write a Python program to calculate the area of a rectangle using the given formula: area = length * width . Take the values of length and width as inputs from the user.

length_of_rectangle = int(input("Enter the Lenght of Rectangle: "))
width_of_rectangle = int(input("Enter the Width of Rectangle: "))
Area_of_rectangle = length_of_rectangle * width_of_rectangle
print(Area_of_rectangle)
print(f"If lenght of a rectangle is {length_of_rectangle} and width of rectangle is {width_of_rectangle} then the area of the rectangle is {length_of_rectangle * width_of_rectangle}")


#Exercise 2:  Write a Python program to demonstrate incrementing and decrementing a variable

price_of_rice = 200
price_of_rice += 50
print(price_of_rice)

price_of_oil = 380
price_of_oil -= 80
print(price_of_oil)


#Exercise 3:  Write a Python program to convert temperature from Celsius to Fahrenheit. The formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as input from the user.

temp_in_celsius = int(input("Enter the temperature in Celsius: "))
temp_in_fahrenheit = ((temp_in_celsius * 9/5) + 32)
print(temp_in_fahrenheit)
print(f"If temperature in celsius is {temp_in_celsius}C, then temperature in Fahrenheit is {((temp_in_celsius * 9/5) + 32)}F ")



#Exercise 4:   Write a Python program to calculate the compound interest given the principal amount, rate, and time (in years).

#amount = principal * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * time)

principal = int(input("Enter the principal amount: "))
rate= int(input("Enter the annual interest rate: "))
rate_of_interest = rate/100
num_compounds_per_year = int(input("Enter the number of times interest compounded per year: "))
time_in_years = int(input("Enter the number of years: "))

compound_interest = print(principal * (1 + rate_of_interest/time_in_years) ** (rate * time_in_years))

print(f"If a person taken a principal of {principal} Rs. for {4} years at a rate of interest {rate}% compounded {num_compounds_per_year} times per year then the total amount to be accured is {(principal * (1 + rate_of_interest/time_in_years) ** (rate * time_in_years))}/. Rs")



#Exercise 5:   Write a Python program to concatenate two strings and display the result. The strings should be taken as input from the user.

student1_name = input("Enter the name of student1: ")
student2_name = input("Enter the name of student2: ")
join = student1_name + student2_name
print(join)


#Exercise 5:   Write a Python program to convert a distance from kilometers to miles.

distance_in_kms = int(input("Enter the distance travelled in Kms: "))
distance_in_miles = distance_in_kms * 0.621
print(distance_in_miles)
print(f"If a person travelled a distance of {distance_in_kms} Km. to go to his school, then he travelled {distance_in_miles} miles.")



##################### Operators Task1 #########################

#Exercise 1:  Create a program that takes user input for their name and age. Use formatted strings (f-strings) to print a message welcoming the user and stating their age.

user_name = input("Enter your name : ")
user_age = int(input("Enter your age : "))
print(f"Hi {user_name}, Welcome to the pythonlife group. We are so happy that at the age of {user_age} years, you joined the group.")


#Exercise 2:  Create a list called numbers that contains integers from 1 to 10.
#Check if the number 5 is in the list.
#Check if the number 15 is not in the list.

roll_no_of_students = [1,2,3,4,5,6,7,8,9,10]
print(5 in roll_no_of_students)
print(15 not in roll_no_of_students)



































































































