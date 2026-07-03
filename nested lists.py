if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        lis = []
        lis.append(name)
        lis.append(score)
        students.append(lis)

    lowest = students[0][1]

    for student in students:
        if student[1] < lowest:
            lowest = student[1]

    sec_low = float('inf')

    for student in students:
        if student[1] > lowest and student[1] < sec_low:
            sec_low = student[1]

    names = []

    for student in students:
        if student[1] == sec_low:
            names.append(student[0])

    names.sort()

    for name in names:
        print(name)
