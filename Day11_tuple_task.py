#  1. Create a Tuple:
#  Write a program that creates a tuple containing three elements: your name, your age, and your favorite color. Then print the tuple.
my_details = ("Pooja", 35, "Blue")
print(my_details)

# 2. Access Tuple Elements:  Write a program that creates a tuple containing the days of the week. Then, print the third element of the tuple.
print(" ")
Days_of_week = ("Sunday","Monday","Tuesday","wednesday","Thursday","Friday","Saturday")
print(f"Third element of the tuple is - {Days_of_week[2]}")

#3.  Tuple Concatenation:  Write a program that creates two tuples, one containing odd numbers from 1 to 5 and another containing even numbers from 2 to 6. 
# Concatenate these two tuples and print the result.
print(" ")
odd_numbers = tuple(i for i in range(1,6) if i%2!=0)
even_numbers = tuple(j for j in range(2,7) if j%2==0)
#concatenation of the two tuples
result = odd_numbers + even_numbers
print(f"Output of the concatenatenated tuples is - {result}")


#4.  Tuple Unpacking: Write a program that defines a tuple containing the dimensions of a rectangle (length and width). 
# Then, unpack this tuple into two variables and calculate the area of the rectangle.
print(" ")
dimen_of_rectangle = (10,5)
length , width = dimen_of_rectangle
print("length", length)
print("width" , width)
area_of_rectangle = length*width
print("Area of the Rectangle", area_of_rectangle)


#5. Check if an Element Exists Write a program that checks if a given element exists in a tuple.
print(" ")
Days_of_week = ("Sunday","Monday","Tuesday","wednesday","Thursday","Friday","Saturday")
if "Sunday" in Days_of_week:
    print("Element Sunday exists in the tuple.")
else:
    print("Element Sunday doesn't exist in the tuple.")


###################################
# Sample Input:
#  items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
# Sample Output:
#  Item#  Price
# -------------------
# Apple   99.00
# Banana  99.00
# Milk    49.00
# -------------------
# Total   247.00

print(" ")
items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
total = 0
print(f"Item\tPrice")
print("-"*20)
for i,j in items:
    print(f"{i}\t{j:.2f}")   #Using concept number:.2f to get the decimal points
    total+=j
print("-"*20)
print(f"Total\t{total:.2f}")































































































































