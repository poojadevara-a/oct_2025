#Task 1:
# Reverse List:
# Write Python code to reverse the order of elements in the given list my_list. 
# Print the reversed list.
# my_list = [10, 20, 30, 40, 50, 11]
# Your code here
# Output should be: [11,50,40,30,20,10]
print(" ")
my_list = [10, 20, 30, 40, 50, 11]
print(f"org list is {my_list}")
#slicing method
print(my_list[::-1])
#reverse order
my_list.reverse()
print(f"reversed list is {my_list}")


#Task 2:
#Common Elements:Given two lists list1 and list2, find and print the common elements between them. 
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# Your code here
## Output should be: [4, 5]
print(" ")
empty_list = []
list1 = [1, 2, 3, 4, 5]
print(f"list1 is {list1}")
list2 = [4, 5, 6, 7, 8]
print(f"list2 is {list2}")
for i in list1:
    for j in list2:
        if i == j:
            empty_list.append(i)
print(f"common elements are {empty_list}")



#Task 3:
#Unique Elements:
#Create a new list unique_list containing only the unique elements from the given list original_list . 
# Print the unique list.
# original_list = [1, 2, 2, 3, 4, 4, 5]
# # Your code here
# # Output should be: [1, 2, 3, 4, 5]
print(" ")
empty_list = []
original_list = [1, 2, 2, 3, 4, 4, 5]
for i in original_list:
    if i not in empty_list:
        empty_list.append(i)
print(f"Unique element are {empty_list}")

#Method 2: List comprehension
result = []
[result.append(i) for i  in [1, 2, 2, 3, 4, 4, 5] if i not in result]
print(result)



#Task 4:
#Remove Duplicates:
#Remove duplicate elements from the given duplicated_list and print the list without duplicates while preserving the order.
#duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# Your code here
# Output should be: [1, 2, 3, 4, 5]
print(" ")
empty_list = []
duplicated_list = [1, 2, 2, 3, 4, 4, 5]

for i in duplicated_list:
        if i not in empty_list:
            empty_list.append(i)
print(empty_list)

#Method 2: List comprehension
result = []
[result.append(i) for i  in [1, 2, 2, 3, 4, 4, 5] if i not in result]
print(result)


#Exercise 1: List Concatenation
#Write a Python script that concatenates two lists and prints the result.
print(" ")
list_1 = ["welcome", "to", "the"]
list_2 = ["python", "life"]
list_1.extend(list_2)
print(list_1)


#Exercise 2:  List Repetition
# Write a Python script that repeats a list three times and prints the result.
print(" ")
animal_list = ["snake", "cat", "frog", "dog", "pig", "tiger"]
sample = []
i=1
while i <=3:
        sample.append(animal_list)
        i+=1
print(sample)


#Exercise 3: List Removal
#Write a Python script that removes the elements at even indices from a list.
print(" ")
list = ["camel", 23, 45, 7.5, "cap", "pot", 34, 76, 43]
print(f"Org list {list}")

print(f"elements at even indices are {list[::2]}")


#Exercise 4: List Insertion
#Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list

print(" ")
list3 = [33,45,78,23,45]
print(f"original data {list3}")
list3.insert(0,10)
print(list3)
list3.insert(1,11)
print(list3)
list3.insert(2,12)
print(list3)
print(f"New modified list {list3}")


########   List comprehensions #########

#Exercise 1: 
#Square Numbers -  Create a list of squares of numbers from 1 to 10.

print(" ")
print([i**2 for i in range(1,11)])

#Exercise 2:
#Even Numbers Generate a list of even numbers from 1 to 20.

print(" ")
result = [i for i in range(1,21) if i%2==0]
print(result)

#Exercise 3:
#Words Length - Given a list of words, create a list containing the lengths of each word.
#words = ["apple", "banana", "cherry", "date"]

print(" ")
words = ["apple", "banana", "cherry", "date"]
sample = [len(words) for words in ["apple", "banana", "cherry", "date"]] 
print(sample)































