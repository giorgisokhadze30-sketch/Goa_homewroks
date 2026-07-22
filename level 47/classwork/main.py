# 1) შექმენით lambda ფუნქცია double, რომელიც არგუმენტად მიიღებს რიცხვს და პასუხად დააბრუნებს გაორმაგებულს.

# 2) შექმენით lambda ფუნქცია check_odd, რომელიც შეამოწმებს რიცხვი კენტია თუ არა. თუ კენტია - აბრუნებს True-ს. სხვა შემთხვევაში False-ს 


def func(n):
    return lambda x: x*n
double = func(2)
print(double(7))


check_odd = lambda x : x%2 !=0

print(check_odd(4))