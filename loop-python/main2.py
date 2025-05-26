# Define a set of elements
elements = {'apple', 'banana', 'cherry', 'date'}

# Convert the set to a list because sets are unordered
# Lists allow indexing, so we can find the position of an element
elements_list = list(elements)

# Ask the user to enter an item to search for
user_input = input("Enter an item to search: ")

# Check if the user input exists in the list
if user_input in elements_list:
    # If found, get the index of the item
    index = elements_list.index(user_input)

    # Print a success message using an f-string
    # f-string is a formatted string 
    # It allows us to embed variables directly in the string using curly braces {}
    print(f"'{user_input}' exists in the set at position {index} in the list.")
else:
    # If not found, print an error message
    print(f"'{user_input}' does not exist in the set.")




#A fixed, direct value in code like "apple" or 42
#Formatted string literal	A directly written string (literal) that includes variables or expressions using {} and starts with f