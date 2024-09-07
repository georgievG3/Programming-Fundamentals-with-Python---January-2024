followers = {}

while True:
    command = input()

    if command == "Log out":
        break

    real_command = command.split(": ")
    action = real_command[0]
    username = real_command[1]

    if action == "New follower":

        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}

    elif action == "Like":
        likes_count = int(real_command[2])

        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}

        followers[username]["likes"] += likes_count

    elif action == "Comment":

        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}

        followers[username]["comments"] += 1

    elif action == "Blocked":

        if username not in followers:
            print(f"{username} doesn't exist.")

        else:
            del followers[username]

print(f"{len(followers)} followers")

for user, info in followers.items():
    sum_likes_comments = 0

    for reaction, count in info.items():
        sum_likes_comments += count

    print(f"{user}: {sum_likes_comments}")
