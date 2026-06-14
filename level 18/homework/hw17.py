
# 18) შექმენით manual sum ფუნქცია Python-ში. (manual ნიშნავს გარკვეული ფუნქციის/მეთოდის საკუთარი ხელით შექმნას.)
# ეს ფუნქცია უნდა მუშაობდეს სიებზე, კონკრეტულად: მან უნდა დააბრუნოს სიის ყველა ელემენტის ჯამი.


def manual_sum(num):
    total = 0
    for i in num:
        total += i
        return total
    
    
    
print(manual_sum([13,12,50]))