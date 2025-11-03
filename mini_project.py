# Dictionary of words
#  Create a program that manages a dictionary of word meanings. The program 
# should allow users to perform the following actions:
#  1. Add a Word: Allow users to add new words along with their meanings to the 
# dictionary.
#  2. Search for Meaning: Enable users to search for the meaning of a word in the 
# dictionary.
#  3. Display All Words: Provide an option to display all words and their meanings 
# currently stored in the dictionary.
#  4. Update Meaning: Implement a feature to update the meaning of an existing 
# word in the dictionary. After updating, display the updated meaning.
#  5. Delete Word: Implement a feature to delete a word and its meaning from the 
# dictionary. Confirm the deletion and handle cases where the word doesn't 
# exist.
#  Ensure the program handles invalid inputs gracefully. Use a while loop to keep the 
# program running until the user chooses to exit.

dictionary = {}

while True:
    print("Dictionary Management System")
    print("1. Add a Word")
    print("2. Search for Meaning: ")
    print("3. Display All Words: ")
    print("4. Update Meaning: ")
    print("5. Delete Word: ")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Word = input("Enter the word: ").lower()
        Meaning = input("Enter the word meaning: ").lower()
        dictionary[Word] = Meaning
        print("\nWord added to the dictionary successfully!")
    elif choice == "2":
        Word = input("\nEnter the word to search: ").lower()
        if Word in dictionary:
            print("Meaning: ", dictionary[Word])
        else:
            print("\nWord not found in the dictionary.")
    elif choice == "3":        
        print(f"\nWords and their meanings: ")
        for i, j in dictionary.items():
            print(f" Word : {i} : {j}")
    elif choice == "4":
        updated_word = input("\nEnter the word to update meaning: ").lower()
        updated_meaning = input("\nEnter the meaning: ").lower()
        dictionary[updated_word] = updated_meaning
        if Word in dictionary:
            print("Meaning updated successfully!")
            print(f"Updated Meaning: {dictionary[updated_word]}")
        else:
            print("\nWord not found in the dictionary.")
    elif choice == "5":
        delete_word = input("\nEnter the word to delete: ")
        if Word in dictionary:
            print("\nWord deleted successfully!")
            print(dictionary.pop(delete_word))
        else:
            print("\nWord not found in the dictionary.")
    elif choice == "6":
        print("\nExiting the Program!!!")
        break
    else:
        print("\nInvalid input. Please try again and enter the numbers from 1 to 6")

    

        






















































































































































































