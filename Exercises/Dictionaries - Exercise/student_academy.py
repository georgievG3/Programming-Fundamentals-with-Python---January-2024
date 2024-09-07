number = int(input())

students_dict = {}

for n in range(number):
    name = input()
    grade = float(input())

    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(grade)

for student_name, grades in students_dict.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student_name} -> {average_grade:.2f}")