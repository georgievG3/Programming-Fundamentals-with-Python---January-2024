def password_validator(password):
    fail_count = 0
    digits = 0
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        fail_count += 1
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        fail_count += 1
    for char in password:
        if char.isdigit():
            digits += 1
    if digits < 2:
        print("Password must have at least 2 digits")
        fail_count += 1
    if fail_count == 0:
        print("Password is valid")


password = input()
password_validator(password)
