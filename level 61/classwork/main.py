# შექმენით Cat კლასი, რომელსაც ექნება ატრიუტები: Breed და Color. მას ასევე დაუმატეთ make_sound მეთოდი, რომელიც გამოძახებისას
# დაბეჭდავს 'Meow'ს. შექმენით მინიმუმ ორი ინსტანცია
# და
# ყველა ატრიბუტი/მეთოდი გამოიძახეთ ტერმინალში.

class Cat:
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color
    
    def make_sound(self):
        print("Meow")
        
        
cat_one = Cat("Bengal" , "Black")

cat_two = Cat("regular" , "White")

# cat_one.make_sound()
# cat_two.make_sound()


print(cat_one.breed)
print(cat_one.color)

cat_one.make_sound()



print(cat_two.breed)
print(cat_two.color)





# 2) შექმენით კლასი iphone, რომელსაც ექნება ატრიუტები: model, price და color. მას ასევე დაუმატეთ pay მეთოდი,
# რომელიც გამოძახებისას დაბეჭდავს 'Succesfully paid {price} dollars to buy {model}' price და მოდელის მაგივრად
# ჩასვით ატრიბუტები საჭირო სინტაქსით. შექმენით 
# მინიმუმ ორი ინსტანცია და ყველა ატრიბუტი/მეთოდი გამოიძახეთ ტერმინალში.


class Iphone:
    def __init__(self,model,price,color):
        self.model = model
        self.price = price
        self.color = color
        
    def pay(self):
        print(f'Succesfully paid {self.price} dollars to buy {self.model}')
        
        
        
        
        

        
iphone_1 = Iphone("17 pro max", "2000", "orange")
iphone_2 = Iphone("16 pro max", "1200" , "black")

iphone_1.pay()

print(iphone_1.model)
print(iphone_1.price)
print(iphone_1.color)

print(iphone_2.model)
print(iphone_2.price)
print(iphone_2.color)