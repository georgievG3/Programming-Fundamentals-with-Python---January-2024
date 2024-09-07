def check_if_palindrome(numbers):
    result = ""
    for number in numbers:
        if str(number) == str(number)[::-1]:
            result += "True\n"
        else:
            result += "False\n"
    return result
numbers = list(map(int, input().split(", ")))
print(check_if_palindrome(numbers))