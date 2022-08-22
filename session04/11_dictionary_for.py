games = {
    "red_redemption_2": 95,
    "gta_5": 93,
    "assassins_creed_brotherhood": 94,
    "fifa_22": 80
}

for key in games:
    print(f"key: {key}, value: {games[key]}")

print()

for key, value in games.items():
    print(f"key: {key}, value: {value}")

print()

for value in games.values():
    print(f"value: {value}")
