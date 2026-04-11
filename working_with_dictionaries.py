car = {
    "model": "Toyota RAV4 Hybrid",
    "price": 1_807_000,
    "engine_volume": 2487,
    "total_weight": 2135,
    "max_speed": 180,
    "fuel_consumption": 4.8,

    "interior_features": [
        "Dual-zone climate control",
        "Heated steering wheel",
        "Power windows",
        "Multimedia system",
        "Rain sensor"
    ],

    "trunk": {
        "volume": 580,
        "volume_with_seats_folded": 1690
    }
}

car["trailer_weight_with_brakes"] = 1500

print("Car model:", car["model"])
print("Price:", car["price"])
print("First interior feature:", car["interior_features"][0])
print("Trunk volume (seats folded):", car["trunk"]["volume_with_seats_folded"])

insurance = car["price"] * 0.005
car["insurance"] = insurance

print("Insurance:", insurance)

gasoline = 93

cost_of_gasoline_for_200km = car.get("fuel_consumption") * 2 * gasoline
print(f"cost of gasoline for 200km: {cost_of_gasoline_for_200km} grn")
