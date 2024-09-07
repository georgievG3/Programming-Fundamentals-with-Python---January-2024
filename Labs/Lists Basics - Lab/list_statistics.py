number = int(input())

positives_list = []
negative_list = []

for n in range(number):
    integers = int(input())
    if integers >= 0:
        positives_list.append(integers)
    else:
        negative_list.append(integers)
count_positives = len(positives_list)
sum_of_negatives = sum(negative_list)

print(f"{positives_list}\n{negative_list}\nCount of positives: {count_positives}\nSum of negatives: {sum_of_negatives}")
