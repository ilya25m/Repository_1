import requests

url = 'https://script.google.com/macros/s/AKfycbxWqm4uoxthsEcYrgEkv9oU9grtiDuvxOiB1OPkgb8N4W_cCUq-3KLQJyM1KukA_a_OXQ/exec'

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