employees_happiness = list(map(int, input().split()))
factor = int(input())


improved_happiness = [number * factor for number in employees_happiness]
average_happiness = sum(improved_happiness) / len(improved_happiness)
happy_count = [happy for happy in improved_happiness if happy >= average_happiness]

if len(happy_count) >= len(improved_happiness) / 2:
    print(f"Score: {len(happy_count)}/{len(improved_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_count)}/{len(improved_happiness)}. Employees are not happy!")