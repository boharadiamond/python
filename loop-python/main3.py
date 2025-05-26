elements = {'1', '2', '4', 5}
elements_list = list(elements)  # Convert set to list

user_input = input("Enter an item to search: ")

try:
    index = elements_list.index(user_input)
    print(f"'{user_input}' exists in the set at position {index} in the list.")
except ValueError:
    print(f"'{user_input}' does not exist in the set.")
