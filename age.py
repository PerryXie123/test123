age = input("Age: ")
a = int(age)
if a <= 0 or a >= 100:
    print("No way")
elif a > 50:
    print("You are older than 50 years old")
elif a < 50:
    print("You are younger than 50 years old")
else:
    print("You are 50 years old")
