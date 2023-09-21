[21/09, 11:03 am] .. ♥️ Agal. Back Bench. ♥️: class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
if __name__ == "__main__":
    # Create a list of student objects
    students = [
        Student("Alice", "A001", 3.8),
        Student("Bob", "B002", 3.6),
        Student("Charlie", "C003", 3.9),
        Student("David", "D004", 3.7),
    ]

    # Sort the students by CGPA in descending order
    sorted_students = sort_students(students)

    # Print the sorted list of students
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
[21/09, 11:05 am] .. ♥️ Agal. Back Bench. ♥️: def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ["apple", "banana", "orange", "apple", "grape", "apple"]
target = "apple"
result = linear_search_product(products, target)
print(result)  # Output: [0, 3, 5]
