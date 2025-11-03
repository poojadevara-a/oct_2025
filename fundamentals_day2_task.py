#Question_1: Write a Python program that prints your name.

print("Pooja")


#Question_2:  Create a Python script with both single-line and multi-line comments explaining the purpose of the script

#below code is performed using addition operation to know total number of tea bags

number_of_new_tea_bags = 20
number_of_old_tea_bags = 30
total_number_of_tea_bags = number_of_new_tea_bags + number_of_old_tea_bags
print(total_number_of_tea_bags)

"""
above code is used to perform addition operation
number_of_new_tea_bags is a variable with a value of 20
number_of_old_tea_bags is a variable with a value of 30
later performed an addition operation using the + operator
result is displayed using the print statement """

#Question_3_a:  Define a list containing three different data types.

list_1 = [2,"chicago", (2,3,"weather")]
print(list_1)
print(type(list_1))

#Question_3_b:  Define a set containing employee idʼs.

Employee_ids = {23457,23478,34568, 45678, 34980}
print(Employee_ids)
print(type(Employee_ids))


#Question_4_a: Concatenate two strings and print the result.

product_1_price = "10"
product_2_price = "30"
print(product_1_price + product_2_price)


#Question_4_b:  Repeat a string three times and display the output.

print('Hello Pooja!')
print("Hello Pooja!")
print('''Hello Pooja!''')


#Question_5: Create a variable with a name that is a Python keyword. What happens? observation..

False = 35
print(False)

"""
I created FAlse as variable and assigned a value 35 to it
later I tried to execute the code using the print statement
the code did not executed and threw mw an error "SyntaxError: cannot assign to False"
this is because False is a reserved word and we can not use this as a variable """


#Question_6: Declare two variables, one storing an integer and the other a string. Print their values.

age = 35
name = "surya"

print(age)
print(name)


#Question_7_a: Convert a float to an integer and print the result.

Height_of_person = 5.3
print(Height_of_person)
print(type(Height_of_person))
int_conversion = int(Height_of_person)
print(int_conversion)
print(type(int_conversion))


#Question_7_b: Convert an integer to a string and display the output.

Employee_id = 23456
print(Employee_id)
print(type(Employee_id))
str_conversion = str(Employee_id)
print(str_conversion)
print(type(str_conversion))


#Question_8: Take the user's age as input and print a message using that input.

user_age = input("Enter the User's age: ")
print(user_age)


###################################################################################


#Question_1: Write a program that prints a pattern using multiple print statements.

print("$")
print("$$")
print("$$$")
print("$$$$")
print("$$$$$$")
print("$$$$$$$")


#Question_2: Create a Python script for a simple task and add comments to explain each step.

number_of_new_tea_bags = 20
number_of_old_tea_bags = 30
total_number_of_tea_bags = number_of_new_tea_bags + number_of_old_tea_bags
print(total_number_of_tea_bags)

"""
above code is used to perform addition operation
number_of_new_tea_bags is a variable with a value of 20
number_of_old_tea_bags is a variable with a value of 30
later performed an addition operation using the + operator
result is displayed using the print statement """


#Question_3:  Implement a program that uses a dictionary to store information about a book (title, author, publication year).

Book = {
    "Title":"Diary of a Wimpy kid", 
    "Author":"Jeff Kinney", 
    "Publication year":"2007"
}
print(Book)
print(type(Book))


#Question_4:  Write a python program that takes a string as input  35  and return float value.

age_of_person2 = "35"
print(age_of_person2)
print(type(age_of_person2))
float_conversion = float(age_of_person2)
print(float_conversion)
print(type(float_conversion))


#Question_5:  Write a program to take two names as input and print them together.

Name = "Pooja","Rishi"
print(Name)


#Question_6:  Create a program that takes user input for their age, converts it to an integer, adds 5, and then prints the result.

User_age = (input("Enter the age of User: "))
int_conversion = int(User_age)
Result = int_conversion + 5
print(Result)


#Question_7: Build a calculator program that takes two numbers as input and performs the arithmetic operation.

num_1 = int(input("Enter Number1: "))
num_2 = int(input("Enter Number2: "))
Total = num_1 + num_2
print(Total)





















