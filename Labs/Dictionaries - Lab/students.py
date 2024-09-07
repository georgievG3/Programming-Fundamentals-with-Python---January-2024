command = input()
students_dict = {}

while ":" in command:
    name, student_id, course = command.split(":")

    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][student_id] = name

    command = input()

course = " ".join(command.split("_"))
for key, value in students_dict.items():
    if key == course:
        for id, name in value.items():
            print(f'{name} - {id}')
