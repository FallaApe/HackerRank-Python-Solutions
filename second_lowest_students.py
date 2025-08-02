# Read number of students
n = int(input("enter number of students"))

students = []  # List to store [name, grade]

# Read student data
for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

# Extract unique grades and find the second lowest
grades = sorted(set([grade for _, grade in students]))
second_lowest = grades[1]

# Get names of students with the second lowest grade
result = sorted([name for name, grade in students if grade == second_lowest])

for name in result:
    print(name)
