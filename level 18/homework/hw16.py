# 17)  შექმენით ფუნქცია, რომელიც პარამეტრად მიიღებს სიას და დააბრუნებს ახალ სიას, სადაც მხოლოდ უნიკალური ელემენტები 
# იქნება — ანუ თქვენი დავალებაა სია გაფილტროთ duplicate ელემენტებისგან.


def filter(name):
    unique = []
    for i in name:
        if i != unique:
            unique.append(i)
    return unique


print(filter([1,2,3,4,5,1,3,7]))
  
