# from collections import defaultdict
#
# students = defaultdict(list)


def calculate_average(iter):
    return sum(iter) / len(iter)


n = int(input())

student_grade = {}

for i in range(n):
    s = input().split()
    student = s[0]
    grade = float(s[1])
    if student not in student_grade:
        student_grade[student] = []
    student_grade[student].append(float(grade))

for (student, grade) in student_grade.items():
    marks = ' '.join(map(lambda grade: f'{grade:.2f}', grade))
                        #(lambda f: format(f, '.2f'), grade)
    avg = calculate_average(grade)
    print(f"{student} -> {marks} (avg: {avg:.2f})")