import random



name = input("Name: ")
random.seed(sum(map(lambda x: ord(x), [*name])))
print(f"You are {random.random() * 100:.0f}% racist")