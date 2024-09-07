some_string = input()
symbol_used = ""
final_string = ""
repetitions = ""

for index in range(len(some_string)):
    if not some_string[index].isdigit():
      symbol_used += some_string[index].upper()
    else:
        for next_symbols in range(index, len(some_string)):
            if not some_string[next_symbols].isdigit():
                break
            repetitions += some_string[next_symbols]
        final_string += symbol_used * int(repetitions)
        repetitions = ""
        symbol_used = ""

print(f"Unique symbols used: {len(set(final_string))}")
print(final_string)
