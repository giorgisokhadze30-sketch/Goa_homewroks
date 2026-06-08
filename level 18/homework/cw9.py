# 10)  შექმენით ფუნქცია check_age, რომელიც არგუმენტად მიიღებს მომხმარებლის ასაკს.
# თუ მომხმარებლის ასაკი მეტი ან ტოლი იქნება 18-ზე, ტერმინალში დაიბეჭდოს "Access Granted", წინააღმდეგ შემთხვევაში
# – "Access Denied".

def check_age(age):
    if age >= 18:
        print("Access Granted")
    else:
        print("Access Denied")
        
        
check_age(14)