# student_system.py

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name}, {self.grade}"

def login():
    USERNAME = "admin"
    PASSWORD = "1234"
    print("===== Login Required =====")
    username = input("Username: ")
    password = input("Password: ")

    if username == USERNAME and password == PASSWORD:
        print("✅ Login successful!")
        return True
    else:
        print("❌ Invalid credentials.")
        return False

def load_from_file(filename="students.csv"):
    students = []
    try:
        with open(filename, "r") as f:
            next(f)  # Skip header
            for line in f:
                name, grade = line.strip().split(",")
                students.append(Student(name, int(grade)))
        print(f"📥 Loaded {len(students)} students from file.")
    except FileNotFoundError:
        print("📁 No existing file found, starting fresh.")
    return students

# ========== Program Entry ==========
if not login():
    exit()

students = load_from_file()
for s in students:
    print(s)
