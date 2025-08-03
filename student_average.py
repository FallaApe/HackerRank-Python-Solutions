if __name__ == '__main__':
    n = int(input("number of students: ")) 
    student_marks = {}

    # Read each student's name and their marks
    for _ in range(n):
        name, *scores = input().split()
        student_marks[name] = list(map(float, scores))  # Convert scores to float

    query_name = input("enter student name: ")  

    # Calculate average marks
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average:.2f}")
