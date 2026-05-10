# 5) შექმენით fruits სია. სიის ბოლოში დაამატეთ 'cherry', სიიდან ამოშალეთ მესამე index-ზე მდგომი
# ელემენტი და მის ნაცვლად (ე.ი მესამე ინდექსზე) დაამატეთ 'Blueberry'.  


fruits = ["Watermelon" ," melon" , "strawberry", "apple"]
fruits.append("cherry")
fruits.pop(3)
fruits.insert(3,"Blueberry")
print(fruits)