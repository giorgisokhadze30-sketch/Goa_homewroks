# 2) შექმენით ცვლადი სადაც შეინახავთ სწორ პაროლს "python123"
# შემდეგ მომხმარებელს შემოაყვანინეთ პაროლი იქამდე სანამ არ შემოიყვანს სწორ პაროლს. 
# თუ არასწორია დაპრინტეთ "Wrong password, try again"
# თუ სწორია დაპრინტეთ "Access granted"
# (გამოიყენეთ while loop და if/else)

correct_password = "python123"

password = input("Enter your password: ")


if password == correct_password :
    print("Acces granted")
else:
    print("Try again")
    


