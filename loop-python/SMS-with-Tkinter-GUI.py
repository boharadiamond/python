import tkinter as tk
from tkinter import messagebox
import csv
import os

# ========== Login Credentials ==========
USERNAME = "admin"
PASSWORD = "1234"

# ========== Load Students from CSV ==========
def load_students(filename="students.csv"):
    students = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    return students

# ========== Main Application Window ==========
def open_main_window():
    def refresh_list(students=None):
        text_box.delete("1.0", tk.END)
        students_list = students if students else load_students()
        if students_list:
            for s in students_list:
                text_box.insert(tk.END, f"{s['Name']} - Grade: {s['Grade']}\n")
        else:
            text_box.insert(tk.END, "No students found.")

    def save_student():
        name = name_entry.get().strip()
        grade = grade_entry.get().strip()
        if not name or not grade:
            messagebox.showerror("Error", "Please fill in both fields.")
            return
        if not grade.isdigit():
            messagebox.showerror("Error", "Grade must be a number.")
            return

        file_exists = os.path.exists("students.csv")
        with open("students.csv", "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Name", "Grade"])
            writer.writerow([name, grade])
        messagebox.showinfo("Success", f"Added student {name}")
        name_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
        refresh_list()

    def delete_student():
        name_to_delete = delete_entry.get().strip()
        if not name_to_delete:
            messagebox.showerror("Error", "Please enter a name to delete.")
            return

        students = load_students()
        updated_students = [s for s in students if s["Name"] != name_to_delete]
        if len(students) == len(updated_students):
            messagebox.showwarning("Not Found", f"No student named '{name_to_delete}' found.")
            return

        with open("students.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Grade"])
            writer.writeheader()
            writer.writerows(updated_students)

        messagebox.showinfo("Deleted", f"Student '{name_to_delete}' removed.")
        delete_entry.delete(0, tk.END)
        refresh_list()

    def search_student():
        keyword = search_entry.get().strip().lower()
        if not keyword:
            messagebox.showerror("Error", "Please enter a name or grade to search.")
            return

        students = load_students()
        results = [s for s in students if keyword in s["Name"].lower() or keyword == s["Grade"]]
        refresh_list(results)

    def update_student():
        name = update_name_entry.get().strip()
        new_grade = update_grade_entry.get().strip()

        if not name or not new_grade:
            messagebox.showerror("Error", "Please enter both name and new grade.")
            return
        if not new_grade.isdigit():
            messagebox.showerror("Error", "New grade must be a number.")
            return

        students = load_students()
        updated = False
        for s in students:
            if s["Name"] == name:
                s["Grade"] = new_grade
                updated = True

        if not updated:
            messagebox.showwarning("Not Found", f"No student named '{name}' found.")
            return

        with open("students.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Grade"])
            writer.writeheader()
            writer.writerows(students)

        messagebox.showinfo("Updated", f"Updated {name}'s grade to {new_grade}")
        update_name_entry.delete(0, tk.END)
        update_grade_entry.delete(0, tk.END)
        refresh_list()

    # ========== GUI Setup ==========
    main_win = tk.Tk()
    main_win.title("Student Management System")
    main_win.geometry("500x700")

    # Scrollable frame setup
    canvas = tk.Canvas(main_win)
    scrollbar = tk.Scrollbar(main_win, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # GUI Content in scrollable_frame
    tk.Label(scrollable_frame, text="Student List", font=("Arial", 16)).pack(pady=10)
    text_box = tk.Text(scrollable_frame, height=10, width=60)
    text_box.pack()
    refresh_list()

    # Add Student Section
    tk.Label(scrollable_frame, text="Add New Student", font=("Arial", 14)).pack(pady=10)
    tk.Label(scrollable_frame, text="Name:").pack()
    name_entry = tk.Entry(scrollable_frame)
    name_entry.pack()
    tk.Label(scrollable_frame, text="Grade:").pack()
    grade_entry = tk.Entry(scrollable_frame)
    grade_entry.pack()
    tk.Button(scrollable_frame, text="Save Student", command=save_student).pack(pady=10)

    # Delete Student Section
    tk.Label(scrollable_frame, text="Delete Student", font=("Arial", 14)).pack(pady=10)
    tk.Label(scrollable_frame, text="Name to Delete:").pack()
    delete_entry = tk.Entry(scrollable_frame)
    delete_entry.pack()
    tk.Button(scrollable_frame, text="Delete Student", command=delete_student).pack(pady=10)

    # Search Student Section
    tk.Label(scrollable_frame, text="Search Student", font=("Arial", 14)).pack(pady=10)
    tk.Label(scrollable_frame, text="Name or Grade:").pack()
    search_entry = tk.Entry(scrollable_frame)
    search_entry.pack()
    tk.Button(scrollable_frame, text="Search", command=search_student).pack(pady=5)
    tk.Button(scrollable_frame, text="Show All", command=refresh_list).pack(pady=5)

    # Update Student Grade Section
    tk.Label(scrollable_frame, text="Update Student Grade", font=("Arial", 14)).pack(pady=10)
    tk.Label(scrollable_frame, text="Name:").pack()
    update_name_entry = tk.Entry(scrollable_frame)
    update_name_entry.pack()
    tk.Label(scrollable_frame, text="New Grade:").pack()
    update_grade_entry = tk.Entry(scrollable_frame)
    update_grade_entry.pack()
    tk.Button(scrollable_frame, text="Update Grade", command=update_student).pack(pady=10)

    main_win.mainloop()

# ========== Login Window ==========
def validate_login():
    user = username_entry.get()
    pw = password_entry.get()
    if user == USERNAME and pw == PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome!")
        root.destroy()
        open_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials!")

root = tk.Tk()
root.title("Login")
root.geometry("300x200")

tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=validate_login).pack(pady=20)

root.mainloop()
