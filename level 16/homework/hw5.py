# 6) მომხმარებელს შემოატანინეთ სიტყვა. შეამოწმეთ არის თუ არა სიტყვის პირველი ასო დიდი. თუ იქნება - გამოიტანეთ 'Perfect', 
# თუ არ იქნება მაშინ გამოუტანეთ 'Your word should be capitalized!'

word = input("Enter your password: ")


if word==word.capitalize():
    print("Perfect")
else:
    print("Your word should be capitalized")