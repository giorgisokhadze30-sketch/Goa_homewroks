# 2) კომენტარის სახით დაწერეთ, თუ რაში ვიყენებთ map და filter ფუნქციებს. მოიყვანეთ თითო მაგალითი.

# map-აიღებს სიას და შეასრულებს მასზე კონკრეტულ მოქმედებებს


def double(res):
     return res * 2

nums = [1,2,3,4]

print(list(map(double , nums)))


# filter კი გამოიყენება გაფილტვრითვის

numbers = [1,2,3,4,5,6,7,8]

evens = list(filter(lambda x: x % 2 == 0, numbers ))
print(evens)






