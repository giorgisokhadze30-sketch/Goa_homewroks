# 1) შექმენით Map კლასი. მიანიჭეთ ატრიბუტები: country, city, IP_location.
# პირველი დონის მონაცემთა დაფარვით - დაფარეთ IP_location და შემდეგ გამოიძახეთ იგი ორივე ნასწავლი გზით.

class Map:
    def __init__(self , country , city ,IP_location ):
        self.country = country
        self.city = city
        self._IP_location = IP_location
        
        
        
info = Map("Georgia" , "Kutaisi" , 1287857872)


print(info._IP_location)





# 2) შექმენით User_data კლასი. მიეცით ატრიბუტები: name, surname, email, password. აქედან email და პაროლი დაფარეთ (Level 1) და გამოიძახეთ ისინი ფუნქციაში დაძახების გზით. შექმენით ორი ცალკეული
# ფუნქცია display_email და display_password


class User_data:
    def __init__(self , name, surname, email, password):
        self.name = name
        self.surname = surname
        self._email = email
        self._password = password
        
    def display_email(self):
            return self._email
        
    def display_password(self):
            return self._password
        
        
        
        
        
data = User_data("Giorgi", "Sokhadze", "giorgisokhadze30@gmail.com", 1235)



print(data.display_email())
print(data.display_password())