import letter

name = input("Введіть ім'я та прізвище: ").strip()
date = input("Введіть дату поїздки: ").strip()
persons = input("Введіть кількість осіб: ")
persons = int(persons)

price_per_person = 15000
total_price = persons * price_per_person

if persons > 5:
    discount = total_price * 0.05
else:
    discount = 0
final_price = total_price - discount

print(letter.LETTER_TEMPLATE.format(name = name, date = date,
persons = persons, price_per_person = price_per_person, total_price = total_price,
discount = discount, final_price = final_price ))