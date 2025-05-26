#for Loops
#Examples:

#Iterating over a list:
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

print('\n')

#Iterating over a string:

for ch in "Hello":
    print(ch)


print('\n')


#Iterating over a range of numbers:
for i in range(3):
      print(i)


print('\n')

#Iterating with indexes:


colors = ['red', 'green', 'blue']
for index in range(len(colors)):
    print(index, colors[index])


print('\n')


#while Loops:
#Examples:

#Counting with while:
count = 0
while count < 3:
    print(count)
    count += 1


print('\n')


#Looping until a condition:

line = input("Enter text (empty to stop): ")
while line != "":
    print("You entered:", line)
    line = input("Enter text (empty to stop): ")

print('\n')


#Infinite loop (until break):

# Simulated data source
def receive_data():
    # Simulate user input; returns empty string to simulate "no more data"
    return input("Enter data (blank to stop): ")

# Simulated processing
def process(data):
    print("Processing:", data)

# Infinite loop (until break)
while True:
    data = receive_data()
    if not data:
        break  # Exit when no more data
    process(data)

print('\n')



#Loop Control Statements (break, continue, pass)
#break – Immediately exits the enclosing loop.
for n in range(1, 6):
    if n == 3:
        break
    print(n)


print('\n')

#continue – Skips to the next iteration.
for n in range(1, 6):
    if n % 2 == 0:
        continue
    print(n)

print('\n')


#pass – Does nothing; acts as a placeholder.
#while True:
#    pass  # Busy-wait or placeholder

#class Empty:
#    pass


print('\n')

 #1. In an unfinished function
def process_data(data):
    pass  # TODO: Implement processing later
#Use case: You're planning to write logic inside process_data, but you're not ready yet. pass avoids a syntax error.

print('\n')

#2. Inside an if/else block

x = 10
if x > 0:
    pass  # Placeholder for future logic
else:
    print("x is not positive")
#Use case: Maybe you only care about the else case for now but don’t want to leave the if block empty


print('\n')


#3. In a class that will be defined later
class Student:
    pass  # Class definition coming soon
#Use case: You're planning to fill in attributes and methods later.

print('\n')


# else Clause with Loops

for i in range(3):
    print(i)
else:
    print("Loop finished without break")

print('\n')

#4. While designing complex structures
for i in range(5):
    if i == 10:
        break
else:
    print("No break occurred")

print('\n')


# Nested Loops
#Example:
#Nested for loops:

for i in [1, 2]:
    for j in [4, 5]:
        print(i, j)

print('\n')

#Nested while loops:
x = [1, 2]
y = [4, 5]
i = 0
while i < len(x):
      j = 0
      while j < len(y):
          print(x[i], y[j])
          j += 1
      i += 1
