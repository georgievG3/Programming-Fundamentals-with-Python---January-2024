vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
string_list = [index for index in input() if index not in vowels]
print("".join(string_list))