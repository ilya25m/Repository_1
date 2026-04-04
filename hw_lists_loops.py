num = [1, 5, 2, 8, 3, 7]

max_num = 0
min_num = 0
total = 0

for num in num:
    total += num

    if max_num == 0 or num > max_num:
        max_num = num

    if min_num == 0 or num < min_num:
        min_num = num

print(f"Найбільше: {max_num}")
print(f"Найменше: {min_num}")
print(f"Сума: {total}")

grades = [10, 8, 12, 7, 9]

total = 0

for grade in grades:
    total += grade

average = total / len(grades)

print(f"Середній бал: {average}")
print("Оцінки вище середнього:")

for grade in grades:
    if grade > average:
        print(grade)