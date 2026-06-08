# 6) შექმენით ფუნქცია და გადაეცით არგუმენტად სია. ფუნქციამ უნდა დააბრუნოს ახალი სია, 
# რომლის თითოეული ელემენტიც უნდა იყოს კვადრატში აყვანილი.


def double_values(list):
    new_list =[]
    for i in list:
        new_list.append(i**2)
    return new_list


print(double_values([1,2,3,4,5]))