# 2) მომხმარებელს შემოატანინეთ 5 რიცხვი და ეტაპობრივად დაამატეთ ისინი სიაში. გამოთვალეთ 
# სიაში შენახულ რიცხვთა საშუალო არითმეტიკული (ფუნქციების გამოყენებით)

list=[]


num1 = int(input("Enter your number: "))
list.append(num1)
num2 = int(input("Enter your number: "))
list.append(num2)
num3 = int(input("Enter your number: "))
list.append(num3)
num4 = int(input("Enter your number: "))
list.append(num4)
num5 = int(input("Enter your number: "))
list.append(num5)

average= sum(list)//len(list)
print(average)



















