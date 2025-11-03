#Task: to find the email names end with "@gmail.com"
email_list = ["example1@gmail.com", "example2@yahoo.com", "example3@gmail.com", "example4@hotmail.com","example5@outlook.com"]

empty_list = []
for i in email_list:
    if i.endswith("@gmail.com"):
        empty_list.append(i)
print(empty_list)

# [exp for item in iter if condition]

print([i for i in empty_list if i in empty_list])


################   Coding Exercise ##################
#Problem 1:
#You are given a string. Example:
# sentence = "Python is amazing"
# Output: "Pto saaig"

print(" ")
sentence = "Python is amazing"
Output = sentence[::2]
print(f"The output is: {Output}")


#Problem 2:
# You are given a string s . Replace all spaces in the string with underscores (_)and print the modified string. Example:
# s = "Python is fun and powerful"
# Output: "Python_is_fun_and_powerful"

print(" ")
s = "Python is fun and powerful"
Output = s.replace(" ","_")
print(f"The output is: {Output}")


#Problem 3:
# You are given a string s. Check if the string contains only digits. Example:

print(" ")
s = "12345"
output = s.isdigit()
print(f"The string contains only digits: {output}")


#Problem 4:
#You are given a string s.  Print the string in reverse order. Example:
#s = "Python is amazing"
# Output: "gnizama si nohtyP

print(" ")
s = "Python is amazing"
Output = s[::-1]
print(f"The output is : {Output}")



#Problem 5:
#You are given a string s.  Capitalize the first letter of each word in the string and print the modified string. Example:
# s = "python programming is fun"
# Output: "Python Programming Is Fun"

print(" ")
s = "python programming is fun"
modified_string = s.title()
print(f"The modified string is: {modified_string}")













































