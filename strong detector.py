import random

NAMES = ["weyman", "perry", "terry", "brian","connor"]
name = input("Name: ")
if name == random.choice(NAMES) or random.random() > 0.5:
    print("is racist")
else:
    print("is not racist")