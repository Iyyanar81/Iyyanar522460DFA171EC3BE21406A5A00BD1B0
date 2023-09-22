class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:

# Creating a list of student objects
students = [
    Student("Alice", "123", 3.7),
    Student("Bob", "456", 3.9),
    Student("Charlie", "789", 3.5),
    Student("David", "101", 4.0),
]

# Sorting the list of students by CGPA
sorted_students = sort_students(students)

# Printing the sorted list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

