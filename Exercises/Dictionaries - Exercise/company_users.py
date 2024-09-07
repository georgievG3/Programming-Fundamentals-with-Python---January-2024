company_dict = {}

while True:
    command = input()

    if command == "End":
        break

    company, employee_id = command.split(" -> ")

    if company not in company_dict:
        company_dict[company] = []

    if employee_id not in company_dict[company]:
        company_dict[company].append(employee_id)


for name, id in company_dict.items():
    print(name)
    for number in id:
        print(f"-- {number}")