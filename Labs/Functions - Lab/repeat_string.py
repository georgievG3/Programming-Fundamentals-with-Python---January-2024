text = input()
counter = int(input())

repeat_string  = lambda a, b: a * b

result = repeat_string(text, counter)
print(result)