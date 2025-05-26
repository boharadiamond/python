# Features:
#Add new students
#
#Display all students
#
#Search for a student
#
#Sort students by grade
#
#Save to file
#
#Delete a student
#
#Update a student's grade
#
#Exit


#Menu-Driven Student Manager (Complete Script)
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}")

    def to_csv(self):
        return f"{self.name},{self.grade}"


def display_all(students):
    if not students:
        print("No student records found.")
    else:
        print("\n📘 All Student Records:")
        for student in students:
            student.display_info()


def add_student(students):
    name = input("Enter student name: ")
    try:
        grade = int(input("Enter grade (0–100): "))
        students.append(Student(name, grade))
        print(" Student added.")
    except ValueError:
        print(" Invalid grade. Please enter a number.")


def search_student(students):
    name = input("Enter name to search: ")
    for student in students:
        if student.name.lower() == name.lower():
            print("🔍 Found:")
            student.display_info()
            return
    print(" Student not found.")


def sort_students(students):
    if not students:
        print("No records to sort.")
        return
    sorted_list = sorted(students, key=lambda s: s.grade, reverse=True)
    print("\n📊 Students sorted by grade (high to low):")
    for student in sorted_list:
        student.display_info()


def save_to_file(students, filename="students.csv"):
    with open(filename, "w") as f:
        f.write("Name,Grade\n")
        for student in students:
            f.write(student.to_csv() + "\n")
    print(f" Saved to '{filename}'.")


def delete_student(students):
    name = input("Enter name to delete: ")
    for student in students:
        if student.name.lower() == name.lower():
            students.remove(student)
            print(f"🗑️ Student '{name}' removed.")
            return
    print(" Student not found.")


def update_student(students):
    name = input("Enter student name to update grade: ")
    for student in students:
        if student.name.lower() == name.lower():
            try:
                new_grade = int(input(f"Enter new grade for {name}: "))
                student.grade = new_grade
                print(" Grade updated.")
            except ValueError:
                print(" Invalid grade.")
            return
    print(" Student not found.")


# Main loop
students = []

while True:
    print("\n====== Student Manager Menu ======")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Sort Students by Grade")
    print("5. Save to File")
    print("6. Delete Student")
    print("7. Update Student Grade")
    print("8. Exit")
    choice = input("Choose an option (1–8): ")

    if choice == '1':
        add_student(students)
    elif choice == '2':
        display_all(students)
    elif choice == '3':
        search_student(students)
    elif choice == '4':
        sort_students(students)
    elif choice == '5':
        save_to_file(students)
    elif choice == '6':
        delete_student(students)
    elif choice == '7':
        update_student(students)
    elif choice == '8':
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print(" Invalid option. Try again.")


# This version is:
#Fully interactive
#
#Easy to extend with more features (e.g., import from file, login system)
#
#Runs in any Python environment (terminal, VS Code, etc.)

