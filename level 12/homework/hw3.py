# 4) დაწერეთ პროგრამა, რომელიც ამოწმებს ტემპერატურას:
# თუ > 30 -> "It's Hot"
# თუ 15-30 -> "It's Warm"
# თუ < 15 -> "It's Cold"

num1 = int(input("Enter your name: "))

if num1 > 30:
    print("It's Hot")
elif 15 <= num1 < 30:
    print("It's Warm")
else:
    print("It's cold")
