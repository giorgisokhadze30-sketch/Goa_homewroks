# 4) შექმენით რიცხვების სია. map-ის გამოყენებით შეინახეთ სიის თითოეული ელემენტი აყვანილი კვადრატში squared სიაში.


nums = [1,2,3,4,5,6,7,8]

squared = list(map(lambda x: x**2, nums))

print(squared)