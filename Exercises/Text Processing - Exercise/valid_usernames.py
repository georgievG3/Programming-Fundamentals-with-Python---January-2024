def valid_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def character_valid(name):
    for character in name:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def redundant_check(name):
    if " " in name:
        return True
    return False


def username_valid(name):
    if valid_length(name) and character_valid(name) and not redundant_check(name):
        return name


usernames = input().split(", ")

for username in usernames:
    if username_valid(username):
        print(username)
