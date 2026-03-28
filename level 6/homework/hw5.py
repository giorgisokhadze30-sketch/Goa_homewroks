#  5) მომხმარებელს შემოატანინეთ 5 რიცხვი. დაწერეთ პროგრამა, რომელიც გამოთვლის და
# დაბეჭდავს ამ რიცხვების საშუალო არითმეტიკულს. 

#  (საშუალო არითმეტიკული = რიცხვთა ჯამის განაყოფი რიცხვების რაოდენობაზე)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter Fourth number: "))
num5 = int(input("Enter fifth number: "))

average  = int(num1+num2+num3+num4+num5)
final = int(average)//5
print(int(final))