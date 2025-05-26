score = 85
if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Very Good")
elif score >= 70:
    print("Good")
else:
    print("Needs Improvement")


print('\n')


age = int(input("Age: "))
if age >= 18:
    country = input("Country: ")
    if country.lower() == "canada":
        print("Adult in Canada")
    else:
        print("Adult outside Canada")
else:
    print("Minor")


print('\n')


def start_process():
    print("Process started.")

def stop_process():
    print("Process stopped.")

def pause_process():
    print("Process paused.")

command = input("Enter command: ")

if command == 'start':
    start_process()
elif command == 'stop':
    stop_process()
elif command == 'pause':
    pause_process()
else:
    print("Unknown command")


print('\n')


import os
from docx import Document

file = input("Filename: ").strip('"')  # Remove quotes if user adds them

if os.path.exists(file):
    if file.lower().endswith('.txt'):
        try:
            with open(file, encoding='utf-8') as f:
                data = f.read()
                print("Text file content:\n", data)
        except UnicodeDecodeError:
            print("Could not read the text file due to encoding issue.")
    elif file.lower().endswith('.docx'):
        try:
            doc = Document(file)
            text = "\n".join([para.text for para in doc.paragraphs])
            print("DOCX file content:\n", text)
        except Exception as e:
            print("Error reading DOCX file:", e)
    else:
        print("Unsupported file type. Only .txt and .docx are allowed.")
else:
    print("File not found.")


print('\n')


class User:
    def __init__(self, is_authenticated, is_admin):
        self.is_authenticated = is_authenticated
        self.is_admin = is_admin

# Create a user
user = User(is_authenticated=True, is_admin=False)

# Check access level
if user.is_authenticated:
    if user.is_admin:
        print("Access granted to admin panel.")
    else:
        print("User does not have admin rights.")
else:
    print("User not logged in.")



'''
| Variable                   | Meaning                  |
| -------------------------- | ------------------------ |
| `is_authenticated = True`  | User is logged in        |
| `is_admin = True`          | User has admin rights    |
| `is_admin = False`         | Regular user (not admin) |
| `is_authenticated = False` | User is not logged in    |


What Output Will You Get?
With this input:
user = User(is_authenticated=True, is_admin=False)
You'll see:
User does not have admin rights.
If you change it to:

user = User(is_authenticated=True, is_admin=True)
You’ll get:

Access granted to admin panel.
If you change it to:

user = User(is_authenticated=False, is_admin=False)
You’ll get:

User not logged in.
'''



    
