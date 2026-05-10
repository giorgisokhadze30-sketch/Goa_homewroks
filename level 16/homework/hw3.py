# 4) მომხმარებლის შეინახეთ password ცვლადში. გამოიყენეთ find ფუნქცია და გაარკვიეთ მომხმარებლის პაროლი
# შეიცავს თუ არა 1-იანს (სტრინგი უნდა იყოს).
# გამოიყენეთ if else-ები (hint: find-ის მიერ დაბრუნებული ინდექსი გამოიყენეთ if-else ში)


password = "Giorgisokhadze123"

answer = password.find("1")

if answer != 1:
    print("Symbol found")
else:
    print("Not found")