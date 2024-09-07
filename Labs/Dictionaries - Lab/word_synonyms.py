number = int(input())
synonyms_dict = {}

for n in range(0, number):
    word = input()
    synonym = input()

    if word not in synonyms_dict:
        synonyms_dict[word] = []
    synonyms_dict[word].append(synonym)

for key in synonyms_dict:
    print(f"{key} - {', '.join(synonyms_dict[key])}")