# Day 18 - Keyword Arguments (Python Intermediate)

def student(name, department, age):
    print("----- Student Details -----")
    print("Name       :", name)
    print("Department :", department)
    print("Age        :", age)

# Keyword Arguments
student(age=18,
        name="Mahizhavarthini",
        department="B.Sc Computer Science")


def employee(name, salary, city):
    print("\n----- Employee Details -----")
    print("Name   :", name)
    print("Salary :", salary)
    print("City   :", city)

# Order doesn't matter in Keyword Arguments
employee(city="Chennai",
         salary=30000,
         name="Rahul")


def multiply(a, b):
    print("\nMultiplication =", a * b)

multiply(b=5, a=8)







----- Student Details -----
Name       : Mahizhavarthini
Department : B.Sc Computer Science
Age        : 18

----- Employee Details -----
Name   : Rahul
Salary : 30000
City   : Chennai

Multiplication = 40