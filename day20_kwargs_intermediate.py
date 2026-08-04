# Day 20 - **kwargs (Python Intermediate)

def student(**details):
    print("----- Student Details -----")

    for key, value in details.items():
        print(key, ":", value)

student(
    name="Mahizhavarthini",
    age=18,
    course="B.Sc Computer Science",
    college="Pavendhar Bharathithasan College"
)





----- Student Details -----
name : Mahizhavarthini
age : 18
course : B.Sc Computer Science
college : Pavendhar Bharathithasan College