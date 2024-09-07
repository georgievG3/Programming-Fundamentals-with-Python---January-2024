results_dict = {}
submissions_dict = {}

while True:
    command = input()

    if command == "exam finished":
        break

    ban_check = command.split("-")

    if ban_check[1] == "banned":
        banned_name = ban_check[0]

        for k, v in results_dict.items():
            for name, score in v.items():
                if name == banned_name:
                    results_dict[k][name] = 0
        continue

    username, language, points = command.split("-")

    if language not in results_dict and language not in submissions_dict:
        results_dict[language] = {}
        submissions_dict[language] = 0

    if username not in results_dict[language]:
        results_dict[language][username] = int(points)

    else:
        if int(points) > results_dict[language][username]:
            results_dict[language][username] = int(points)

    submissions_dict[language] += 1

print("Results:")
for language_name, result in results_dict.items():
    for participant_name, participant_points in result.items():
        if results_dict[language_name][participant_name]:
            print(f"{participant_name} | {participant_points}")
print("Submissions:")
for submission_language in submissions_dict:
    print(f"{submission_language} - {submissions_dict[submission_language]}")