Day 13 - Python Dictionary Basics Practice



# Day 13 - Dictionary Basics

student = {
    "name": "Mahizhavarthini",
    "age": 18,
    "course": "B.Sc Computer Science"
}

print("Student Details:", student)
print("Name:", student["name"])
print("Age:", student.get("age"))
print("Course:", student["course"])

print("Total Items:", len(student))
print("Keys:", student.keys())
print("Values:", student.values())




Student Details: {'name': 'Mahizhavarthini', 'age': 18, 'course': 'B.Sc Computer Science'}
Name: Mahizhavarthini
Age: 18
Course: B.Sc Computer Science
Total Items: 3
Keys: dict_keys(['name', 'age', 'course'])
Values: dict_values(['Mahizhavarthini', 18, 'B.Sc Computer Science'])