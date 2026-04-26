# 5) მოხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ:
# • "Positive even"
# • "Positive odd"
# • "Negative"

num2 = int(input("Enter your number: "))

if num2 < 0:
    print("Negative")
elif num2 % 2 == 0:
    print("Positive even")
else:
    print("Positive odd")
    