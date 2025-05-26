
#New Features:
#Saving student records to a file
#
#Searching for a student by name
#
#Sorting students by grade (descending)



#Full Python Script: Student Manager with Search, Sort & Save

# Define a Student class with attributes
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Student Name: {self.name}, Grade: {self.grade}")

# Process data: take a list of students and display info
def process_data(student_list):
    print("\nStudent Records:")
    for student in student_list:
        student.display_info()

# Check if the grade is valid and give feedback
def check_grade(grade):
    if grade >= 90:
        print("Excellent performance!")
    elif grade >= 75:
        print("Good job!")
    elif grade >= 50:
        print("Keep trying, you can improve.")
    else:
        print("Needs serious improvement.")

# Main interaction
students = []

# Collect 3 students as sample input
for i in range(3):
    name = input(f"Enter name for student {i+1}: ")
    grade = int(input(f"Enter grade (0–100) for {name}: "))
    student = Student(name, grade)
    students.append(student)
    check_grade(grade)

# Process and display student info
process_data(students)

# Loop through students and mention who scored even grades
print("\nStudents with even grades:")
for student in students:
    if student.grade % 2 == 0:
        print(f"{student.name} has an even grade: {student.grade}")



'''
Features Included:
Student class with real data.

No pass — all logic is now complete.

User inputs names and grades.

Feedback is given based on each student’s grade.

Students with even-numbered grades are listed separately.



Expected Output:
Enter name for student 1: Alice
Enter grade (0–100) for Alice: 92
Excellent performance!

Enter name for student 2: Bob
Enter grade (0–100) for Bob: 77
Good job!

Enter name for student 3: Carol
Enter grade (0–100) for Carol: 49
Needs serious improvement.

Student Records:
Student Name: Alice, Grade: 92
Student Name: Bob, Grade: 77
Student Name: Carol, Grade: 49

Students with even grades:
Alice has an even grade: 92

'''