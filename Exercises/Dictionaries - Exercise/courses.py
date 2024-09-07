courses_dict = {}

while True:
    command = input()

    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    if course_name not in courses_dict:
        courses_dict[course_name] = {"Students_count": 0, "Students": []}
    courses_dict[course_name]["Students_count"] += 1
    courses_dict[course_name]["Students"].append(student_name)

for course, info in courses_dict.items():
    print(f"{course}: {info['Students_count']}")
    for name in info['Students']:
        print(f"-- {name}")