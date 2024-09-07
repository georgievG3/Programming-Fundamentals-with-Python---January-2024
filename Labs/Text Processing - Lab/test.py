text = "hello world"
result = "".join([char.upper() if char.islower() else char.lower() for char in text])
print(result)