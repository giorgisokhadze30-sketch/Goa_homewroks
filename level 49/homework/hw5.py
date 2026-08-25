# 6) შექმენით Dict, მასში შეინახეთ key და value წყვილებად მანქანის დასახელება და მისი გამოშვების წელი. გამოიყენეთ filter,
# რომ old_years ცვლადში შეინახოთ მხოლოდ
# 2000-წლამდე გამოშვებული მანქანები (სიის სახით).


cars = {
    "BMW": 1998,
    "Mercedes": 2005,
    "Audi": 1995,
    "Toyota": 2010,
    "Ford": 1999
}

old_years = list(filter(lambda item: item[1] < 2000, cars.items()))


print(old_years)