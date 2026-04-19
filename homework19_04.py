import requests
from pprint import pprint

url = 'https://dummyjson.com/recipes'
params = {
    "skip": 0,
    "limit": 1000,
}

response = requests.get(url=url, params=params)
response_json = response.json()
recipes = response_json['recipes']

pizza_recipes = []
italian_count = 0
most_calorie = 0
most_calorie_name = ""
recipes_190 = []
total_reviews = 0

for recipe in recipes:

    name = recipe['name']
    cuisine = recipe['cuisine']
    calories = recipe['caloriesPerServing']
    instructions = recipe['instructions']
    reviews = recipe['reviewCount']

    if "pizza" in name.lower():
        pizza_recipes.append(name)

    if cuisine == "Italian":
        italian_count = italian_count + 1

    if calories > most_calorie:
        most_calorie = calories
        most_calorie_name = name

    if instructions:
        first_step = instructions[0]
        if "190" in first_step:
            recipes_190.append(name)

    total_reviews = total_reviews + reviews


print("Пиццы:")
pprint(pizza_recipes)

print("Итальянских блюд:", italian_count)

print("Самое калорийное блюдо:")
print(most_calorie_name, most_calorie)

print("Готовятся при 190°C:")
pprint(recipes_190)

print("Всего отзывов:", total_reviews)