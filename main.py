from pywebio.input import input, slider, select
from pywebio.output import put_markdown, put_text, put_image
import pictures
import prices
import math
from prices import PRICE_TRAIN, PRICE_HOTEL

put_markdown("Шкільні поїздки")
put_markdown("---")
put_markdown("## Тип транспорту:")

put_image(pictures.PICTURE_BUS)
put_text(f"""🚌 Автобус:
1 автобус = 40 місць
ціна = {prices.PRICE_BUS} грн за автобус (за всю поїздку)""")

put_image(pictures.PICTURE_TRAIN)
put_text(f"""🚆 Поїзд:
1 людина = {prices.PRICE_TRAIN} грн (в обидві сторони)""")

put_text(f"""🏨 Проживання:
1 людина = {prices.PRICE_HOTEL} грн / ніч""")

quantity_students = slider(label="Введіть кількість учнів:", min_value=0, max_value=140, value=1, step=1)
quantity_teachers = slider(label="Введіть кількість вчителів:", min_value=0, max_value=20, value=1, step=1)
quantity_days = slider(label="Оберіть кількість днів:", min_value=0, max_value=7, value=1, step=1)
transport = select("Оберіть транспорт:", ["Автобус", "Поїзд"])

if quantity_students == 0:
        put_text("❌ Помилка: кількість учнів не може бути 0")

quantity_people = quantity_students + quantity_teachers
if transport == "Автобус":
    total_price_transport = quantity_people * prices.PRICE_BUS
    quantity_bus = math.ceil(quantity_people /40)
else:
    total_price_transport = quantity_people * prices.PRICE_TRAIN
    quantity_bus = 0

if quantity_days >0:
    total_price_hotel = quantity_people * prices.PRICE_HOTEL
else:
    total_price_hotel = 0
total_price = total_price_hotel + total_price_transport
discount = 0
if quantity_people >30:
    discount = total_price * 0.10
total_price = total_price - discount

put_markdown("---")
put_text(f"""Загальна кількість людей: {quantity_people}
Транспорт: {transport}
Кількість автобусів (якщо є): {quantity_bus}
Вартісь транспорту: {total_price_transport} грн
Вартість проживання: {total_price_hotel} грн
Знижка: {discount} грн
Загальна вартість: {total_price} грн
""")