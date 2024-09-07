words_list = input().split()
palindrome = input()

palindrome_found_list = [word for word in words_list if word == word[::-1]]
palindrome_found = sum(1 for word in words_list if palindrome == word)


print(palindrome_found_list)
print(f"Found palindrome {palindrome_found} times")