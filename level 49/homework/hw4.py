# 5) 5 მომხმარებელს შემოატანინეთ სახელი input-ით, შემდეგ კი შეინახეთ usernames სიაში.
# გამოიყენეთ map, იმისთვის რომ თითოეულ სახელს წინ დაუწეროთ "Welcome". განახლებული შედეგი შეინახეთ სიაში სახელწოდებით 
# greet_users.

usernames = []
for i in range(5):
    name = input(f"put your username {i + 1}: ")
    usernames.append(name)


greet_users = list(map(lambda name: "Welcome " + name, usernames))


print(greet_users)