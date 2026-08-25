# 7) 5 მომხმარებელს შემოატანინეთ სახელი input-ით, შემდეგ კი შეინახეთ usernames სიაში. 
# გამოიყენეთ filter, რომ filtered_users სიაში მხოლოდ შეინახოთ სახელები, რომელთა სიმბოლოების რაოდენობაც 5-ს აღემატება.

usernames = []
for i in range(5):
    name = input(f"put your username {i + 1}: ")
    usernames.append(name)

filtered_users = list(filter(lambda name: len(name) > 5, usernames))

print(filtered_users)