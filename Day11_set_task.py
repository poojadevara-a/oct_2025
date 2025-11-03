
#### Class Task ####
# Taking one normal set and one frozen set and performed the operations ke union, intersection, symmetris diff, diff.
set1 = {1,2,3,4,5}
print(set1)
set2 = frozenset(set1)
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.difference(set2))


# Task 1: Set Intersection
# Write Python code to find and print the intersection of the following two sets:
#  set1 = {1, 2, 3, 4, 5}
#  set2 = {4, 5, 6, 7, 8}
#  Your code here
# Output should be: {4, 5}
print(" ")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))


#  Task 2: Set Union
#  Write Python code to find and print the union of the following two sets:
#  set1 = {1, 2, 3, 4, 5}
#  set2 = {4, 5, 6, 7, 8}
#  Your code here
# Output should be: {1, 2, 3, 4, 5, 6, 7, 8}
print(" ")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))


#   Task 3: Set Difference
#  Write Python code to find and print the elements present in  set1 but not in set2
#  set1 = {1, 2, 3, 4, 5}
#  set2 = {4, 5, 6, 7, 8}
#  Your code here
# Output should be: {1, 2, 3}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.difference(set2))


#  Task 4: Set Symmetric Difference
#  Write Python code to find and print the symmetric difference of the following two sets:
#  set1 = {1, 2, 3, 4, 5}
#  set2 = {4, 5, 6, 7, 8}
#  Your code here
# Output should be: {1, 2, 3, 6, 7, 8}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.symmetric_difference(set2))


#   Task 5: Set Membership Test
#   Write Python code to check if the element 3 is present in the set my_set 
#  my_set = {1, 2, 3, 4, 5}
# Your code here
# Output should be: True
my_set = {1, 2, 3, 4, 5}
if 3 in my_set:
    print(f"Element 3 present in {my_set}")
else:
    print(f"Element 3 is not present in {my_set}")




































































































































