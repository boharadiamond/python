#Arithmetic Operators

a = 7
b = 2
print(a + b)   # 9   (addition)
print(a - b)   # 5   (subtraction)
print(a * b)   # 14  (multiplication)
print(a / b)   # 3.5 (division, float result)
print(a // b)  # 3   (floor division)
print(a % b)   # 1   (modulo, remainder)
print(a ** b)  # 49  (exponentiation)


print('\n')

#Comparison Operators

a = 5
b = 2
print(a == b)  # False  (5 is not equal to 2)
print(a != b)  # True   (5 is not equal to 2)
print(a > b)   # True   (5 is greater than 2)
print(a < b)   # False  (5 is not less than 2)
print(a >= b)  # True   (5 is greater than or equal to 2)
print(a <= b)  # False  (5 is not less than or equal to 2)



print('\n')

#Logical Operators

print(True and True)   # True   (both are true)
print(True and False)  # False  (one is false)
print(True or False)   # True   (at least one is true)
print(False or False)  # False  (neither is true)
print(not True)        # False  (logical NOT)
print(not False)       # True


print('\n')

#Assignment Operators

x = 10   # assign 10 to x
print(x)  # 10

x += 5   # same as x = x + 5
print(x)  # 15

x *= 2   # same as x = x * 2
print(x)  # 30

x -= 10  # same as x = x - 10
print(x)  # 20

x //= 3  # same as x = x // 3 (floor division)
print(x)  # 6

x %= 4   # same as x = x % 4 (remainder)
print(x)  # 2

x **= 3  # same as x = x ** 3 (exponent)
print(x)  # 8


print('\n')

#Bitwise Operators

x = 5  # (binary 0101)
y = 3  # (binary 0011)
print(x & y)  # 1   (binary 0001)
print(x | y)  # 7   (binary 0111)
print(x ^ y)  # 6   (binary 0110)
print(~x)     # -6  (binary ...1010 in two's complement)
print(x << 1) # 10  (binary 1010)
print(x >> 1) # 2   (binary 0010)


print('\n')

#User Input with input()

name = input("What is your name? ")
print("Hello, " + name + "!")


print('\n')


num_str = input("Enter a number: ")
num_int = int(num_str)        # convert to integer
print("Twice your number is", num_int * 2)


print('\n')


# Or more concisely:
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)








