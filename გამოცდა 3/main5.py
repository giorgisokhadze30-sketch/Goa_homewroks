# 5) დაწერეთ ფუნქცია რომელიც მიიღებს მომხმარებლის სახელს. გვარსა და ასაკს. ფუნქციამ დააბრუნოს მომხმარებლის
# მონაცემები f სტრინგის გამოყენებით


def user_info(name,surname,age):
    return f"name:{name}, surname:{surname}, age:{age}"



print(user_info("Giorgi","Sokhadze",16))