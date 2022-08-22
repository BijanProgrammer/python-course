games = {
    "red_redemption_2": 95,
    "gta_5": 93,
    "assassins_creed_brotherhood": 94,
    "fifa_22": 80
}

print(games["red_redemption_2"])  # throws an error if key is not found
print(games.get("red_redemption_2"))  # returns None if key is not found

games["fifa_22"] = 82

games.pop("assassins_creed_brotherhood")
print(games)
