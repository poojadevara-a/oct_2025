#Problem 1: Using break in a While Loop
#Write a Python program that takes a list of numbers as input 
#numbers = [25, 30, 20, 40, 15, 25] and prints the sum of the numbers. 
# However, if the sum exceeds 100, stop adding numbers and print "Sum exceeded 100".

numbers = [25, 30, 20, 40, 15, 25]
sum = 0
for i in numbers:
    sum+=i
    if sum > 100:
        print("Sum exceeded 100")
        break
print(f"Last iterative num {i}")
print(f"Sum of numbers {sum}")


#Problem 2: Using continue in a For Loop
#Write a Python script that uses a for loop to iterate through numbers from 1 to 600. 
#Print only the odd numbers, skipping the even ones using the statement.

for i in range(1,601):
    if i%2 == 0:
        continue
    print(i)


#Problem 3: Using pass in Conditional Statements continue 
#Write a Python script that checks if a number is even or odd. 
# If the number is even, print "Even"; 
# if odd, do nothing (use the pass statement)

number = int(input("Enter the number: "))
if number%2==0:
    print("Even")
elif number%2!=0:
    pass
else:
    print("Invalid input")
     


#Problem 4: Combining Transfer Statements
#Write a Python script that iterates through a list of words. 
#If the word is "break," exit the loop using the break statement. 
#If the word is "skip," skip the rest of the code for the current iteration using the continue statement. 
#For any other word, print the word.

#4(a) Here as i mentioned skip before the break, the output is apple, pooja, jack
words = ["apple", "pooja", "skip", "jack", "break","flag", "kiwi", "water"]

for i in words:
    if i == "break":
        break
    elif i == "skip":
        continue
    else:
        print(i)

#4(b) Here as i jumbled the words and first wrote break later skip. so the output is apple, pooja.
words = ["apple", "pooja", "break", "jack", "flag", "skip", "kiwi", "water"]

for i in words:
    if i == "break":
        break
    elif i == "skip":
        continue
    else:
        print(i)

#################Transfer statements practice#############

################Break#########################

for i in range(11):
    if i == 6:
        break
    print(i)
print(f"last iteration value {i}")



for i in range(11):
    if i == 6:
        print(i)
print(f"last iteration value {i}")



emp_data = ["achyuth","anudeep","pooja","tejasree","kowshik","veena","vishnu"]
for i in emp_data:
    if i == "pooja":
        print(i)
print(f"Last iteration value {i}")
#here there are only 7 elements. so even after kowshik condition met, it will iterate till the last value vishnu and then stops.

#What if there are 1000 to 30000 elements, in such situations, eventhough the condition is met, if it still iterates till the end it will take lot of time to execute the code. so we use break statemnet there. so when the condition is met, it will break the block of code
emp_data = ["achyuth","anudeep","pooja","tejasree","kowshik","veena","vishnu"]
for i in emp_data:
    if i == "pooja":
        print(i)
        break
print(f"Last iteration value {i}")


######Continue#######
#continue skips only that specific condition, but it doesnt stop looping. loopinf continues till the end.
for i in range(5):
    if i == 3:
        continue
    print(i)


emp_data = ["achyuth","anudeep","pooja","tejasree","kowshik","veena","vishnu"]
for i in emp_data:
    if i == "pooja":
        continue
    print(i)


product = ["ok","ok","ok","defect","defect","ok","ok","defect","ok"]
for i in product:
    if i == "defect":
        continue
    print(i)


###########Pass##############
#Just to hold the place, when i dono what requirement my clent needs. it just holds the place.
#It does iterations and looping also completes....But it doesnt perform any operations.

for i in range(5):
    pass
print(f"last iteration {i}")


######Practicing python list, indexing, slicing############

######Practicing python list, indexing, slicing############

sample = "pythonlife"
print(sample[6]) #l
print(sample[4]) #o

list = [10,20,30,40,50]
#this is positive indexing. It goes in forward direction and starts from zero.
print(list[3]) #40
print(list[4]) #50
print(list[0]) #10
print(list[2]) #30


list_1 = [10,20,30,40,50,60]
#this is negative indexing. It starts in back ward direction. Starts from -1 and goes till -n
print(list_1[3]) #40  positive indexing
print(list_1[-3]) #40  negative indexing
print(list_1[0]) #10  positive indexing
print(list_1[-6]) #10  negative indexing
print(list_1[2]) #30  positive indexing
print(list_1[-4]) #30  negative indexing

##slicing####

list_3 = [10,20,30,40,50,60,70,80]
#if i want to access from 20 to 40 then
#seq[start:stop:step]
print(list_3[1:4]) #20,30,40
print(list_3[5:8]) #60,70,80
print(list_3[:]) #10,20,30,40,50,60,70,80
print(list_3[0:8]) #10,20,30,40,50,60,70,80
print(list_3[0:8:2]) #10, 30, 50, 70
print(list_3[0:8:3]) #10, 40, 70
print(list_3[0:8:4]) #10, 50

#if we dnt give start value, it defaultly takes 0 and end value if we dnt gives takes the last value
print(list_3[::]) #10,20,30,40,50,60,70,80
print(list_3[:3]) #10,20,30,
print(list_3[5:]) #60,70,80

list_3 = [10,20,30,40,50,60,70,80]
#negative indexing
print(list_3[4:7]) #50, 60, 70 positive indexing
print(list_3[-4:-1]) #50, 60, 70 negative indexing
print(list_3[-7:-4]) #20, 30, 40 negative indexing
print(list_3[-3:]) #60, 70, 80 negative indexing

##Slicing backward direction########
#Backward direction is always RHS , to do this always step is -1
list_3 = [10,20,30,40,50,60,70,80]
print(list_3[::-1]) #80, 70, 60, 50, 40, 30, 20, 10
print(list_3[4:1:-1]) #50,40,30 in forward direction reverse order
print(list_3[:4:-1]) #80, 70, 60 in forward direction positive indexing reverse order 
print(list_3[7:4:-1]) #80, 70, 60 in forward direction positive indexing reverse order 
print(list_3[2::-1]) #30,20,10 in forward direction positive indexing reverse order 
print(list_3[5:2:-1]) #60,50,40 in forward direction positive indexing reverse order 
print(list_3[-3:-6:-1]) #60,50,40 in Backward direction negative indexing in reverse order
print(list_3[-5:-8:-1]) #40, 30, 20 in Backward direction negative indexing in reverse order
print(list_3[-5::-1]) #40, 30, 20, 10 in Backward direction negative indexing in reverse order
print(list_3[:-3:-1]) #80, 70 in Backward direction negative indexing in reverse order
print(list_3[-1:-3:-1]) #80, 70 in Backward direction negative indexing in reverse order


























