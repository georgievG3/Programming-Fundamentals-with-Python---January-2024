schedule_lessons_list = input().split(", ")

command = input()
while command != "course start":
    main_command = command.split(":")
    if main_command[0] == "course start":
        break
    command_type = main_command[0]
    index = main_command[-1]

    if command_type == "Add" and main_command[1] not in schedule_lessons_list:
        schedule_lessons_list.append(main_command[1])
    elif command_type == "Insert" and main_command[1] not in schedule_lessons_list:
        lesson_title = main_command[1]
        lesson_exercise = f"{lesson_title}-Exercise"
        if lesson_exercise in schedule_lessons_list:
            index1 = schedule_lessons_list.index(lesson_exercise)
            schedule_lessons_list.insert(index1, lesson_title)
        else:
            schedule_lessons_list.insert(int(index), main_command[1])
    elif command_type == "Remove" and main_command[1] in schedule_lessons_list:
        lesson = main_command[1]
        lesson_exercise = f"{lesson}-Exercise"
        if lesson_exercise in schedule_lessons_list:
            schedule_lessons_list.remove(lesson_exercise)
        schedule_lessons_list.remove(lesson)
    elif command_type == 'Swap':
        lesson_title, swap_title = main_command[1], main_command[2]
        lesson_exercise = f'{lesson_title}-Exercise'
        swap_exercise = f'{swap_title}-Exercise'
        if lesson_title in schedule_lessons_list and swap_title in schedule_lessons_list:
            index_one = schedule_lessons_list.index(lesson_title)
            index_two = schedule_lessons_list.index(swap_title)
            schedule_lessons_list[index_one], schedule_lessons_list[index_two] = schedule_lessons_list[index_two], schedule_lessons_list[
                index_one]
        if lesson_exercise in schedule_lessons_list:
            # index_one_exercise = initial_schedule.index(lesson_exercise)
            schedule_lessons_list.remove(lesson_exercise)
            initial_schedule = schedule_lessons_list[:index_two + 1] + [lesson_exercise] + schedule_lessons_list[index_two + 1:]
        if swap_exercise in schedule_lessons_list:
            # index_swap_exercise = initial_schedule.index(swap_exercise)
            schedule_lessons_list.remove(swap_exercise)
            schedule_lessons_list = schedule_lessons_list[:index_one + 1] + [swap_exercise] + schedule_lessons_list[index_one + 1:]
    elif command_type == "Exercise":
        lesson_title = main_command[1]
        lesson_exercise = f"{lesson_title}-Exercise"
        if lesson_title in schedule_lessons_list and lesson_exercise not in schedule_lessons_list:
            index1 = schedule_lessons_list.index(lesson_title)
            if lesson_exercise not in schedule_lessons_list:
                schedule_lessons_list.insert(index1 + 1, lesson_exercise)
        elif lesson_title not in schedule_lessons_list:
            if lesson_exercise in schedule_lessons_list:
                index1 = schedule_lessons_list.index(lesson_exercise)
                schedule_lessons_list.insert(index1, lesson_title)
            else:
                schedule_lessons_list.append(lesson_title)
                schedule_lessons_list.append(lesson_exercise)
    command = input()

for i in range(len(schedule_lessons_list)):
    print(f'{i + 1}.{schedule_lessons_list[i]}')
