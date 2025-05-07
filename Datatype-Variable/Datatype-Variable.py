name0='diamond'
print(name0)



x0 = 5           # x refers to an integer object (int)
y = "Alice"     # y refers to a string object (str)
print(x0)
print(y)


x1 = 10          # x is now int
x2 = "hello"     # x is now str (dynamic typing)
print(x1)
print(x2)



name1 = "Jane"
age = 30
fruits = ["apple", "banana"]
print(type(name1))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(fruits))  # <class 'list'>



a = 5          # int
b = 3.14       # float
c = 2 + 4j     # complex
print(type(a), type(b), type(c))




s = "Hello, World!"
print(type(s))     # <class 'str'>
print(s[7:12])     # "World"



flag = True
print(type(flag))  # <class 'bool'>
print(1 + True)    # 2, since True == 1




fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # <class 'list'>




fruits.append("date")
fruits[1] = "blueberry"
print(fruits)  # e.g. ['apple', 'blueberry', 'cherry', 'date']




coord = (10, 20)       # tuple of two ints
point = 1, 2, 3        # also a tuple of three ints (parentheses optional)
print(type(coord))     # <class 'tuple'>



languages = {"Python", "Java", "C++"}
print(type(languages))  # <class 'set'>




nums = {1, 2, 3}
nums.add(4)
nums.remove(2)
print(nums)  # e.g. {1, 3, 4}





person = {"name": "Alice", "age": 30}
print(type(person))   # <class 'dict'>



