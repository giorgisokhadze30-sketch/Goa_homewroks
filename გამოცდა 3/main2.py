# 2)შექმენით ისეთი ფუნქცია რომელიც  შეამოწმებს თუ მოხმარებელის ასაკი მეტია 18 ზე უნდა დაუბეჭდოთ# "you can enter" და თ ნაკლებია 
# "you are still child
    ##
    
    
    
    
def check_age(age):
    if age > 18:
        return "You can enter"
    else:
        return "You are still child"
    
    
print(check_age(15))
print(check_age(19))