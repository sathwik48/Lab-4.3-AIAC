class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = float(marks)

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'Fail'

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")

# Read data from console
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Add error handling for marks input
while True:
    try:
        marks = input("Enter marks: ")
        marks_float = float(marks)
        if 0 <= marks_float <= 100:
            break
        else:
            print("Marks must be between 0 and 100. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number for marks.")

# Create Student object and display details
student = Student(name, roll_no, marks_float)
student.display_details()
