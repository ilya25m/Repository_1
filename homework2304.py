import requests

url = 'https://script.google.com/macros/s/AKfycbxQWk9n4Ozxkq2HNfNPbVZXwAirgmUAqRZU-eX7Fj86a_5RuhOqo6m0PeghvitskXiM5w/exec'

response = requests.get(url=url, params={})
data = response.json()

animals = data['animals']

venomous_cost = 0

for row in animals:
    if row['is_venomous'] == 'yes':
        venomous_cost += float(row['care_cost']) * int(row['count'])

print("Venomous animals care cost:", venomous_cost)


african_count = 0

for row in animals:
    if row['continent'] == 'Africa':
        african_count += int(row['count'])

print("Number of African animals:", african_count)