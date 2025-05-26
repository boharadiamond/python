elements = ['apple', 'banana', 'cherry', 'date']

user_input = input("Enter an item to search: ")

if user_input in elements:
    position = elements.index(user_input)
    print(f"'{user_input}' found at position {position}.")
else:
    print(f"'{user_input}' not found in the list.")
