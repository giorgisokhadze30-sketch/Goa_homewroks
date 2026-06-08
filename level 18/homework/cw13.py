# 14) დაწერეთ ფუნქცია, რომელიც არგუმენტად მიიღებს მომხმარებლის სახელს, გვარს და ასაკს. 
# ფუნქციამ უნდა დააბრუნოს მომხმარებლის მონაცემები წინადადების სახით. (გამოიყენეთ f string-ი)


def personal_info(name,surname,age):
    return f"hello my name is {name}, my surname is {surname}, and i am {age} years old"


print(personal_info("Giorgi","sokhadze",16))
    