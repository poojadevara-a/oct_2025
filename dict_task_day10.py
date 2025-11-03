## Task 1: Dictionary Update
# Write Python code to add a new key-value pair to the following dictionary:
# my_dict = {'name': 'python', 'age': 25}
# Your code here
# Output should be: {'name': 'python', 'age': 25, 'city': 'west godavari'}

my_dict1 = {'name': 'python', 'age': 25}
new_word = my_dict1['city'] = 'west godavari'
print(f"Updated dictionary is {my_dict1}")


## Task 2: Dictionary Access
# Write Python code to access and print the value associated with the key 'price' in the following dictionary:
# product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
# Your code here
# Output should be: 1200
print(" ")
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(f"The value associated with the key 'price' is : {product_info.get('price')}")


## Task 3: Dictionary Removal
# Write Python code to remove the key-value pair with the key 'city' from the following dictionary:
# my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
# Your code here
# Output should be: {'name': 'John', 'age': 30}
print(" ")
my_dict3 = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
remove = my_dict3.pop('city')
print(my_dict3)


## Task 4: Dictionary Keys
# Write Python code to print all the keys present in the following dictionary:
# my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
# Your code here
# Output should be: ['name', 'age', 'city']
print(" ")
my_dict4 = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(f"The keys of the dictionary are {my_dict4.keys()}")


##  Task 5: Dictionary Values
# Write Python code to print all the values present in the following dictionary: 
#  my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
# Your code here
# Output should be: ['python', 25, 'tanuku']
print(" ")
my_dict5 = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(f"The values of the dictionary are {my_dict5.values()}")













































































































































































