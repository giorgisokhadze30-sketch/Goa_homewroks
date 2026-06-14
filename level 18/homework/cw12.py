# 13) შექმენით ფუნქცია student_grade, რომელიც იღებს მოსწავლის ქულას (0-დან 100-მდე) და ტერმინალში დაბეჭდავს შემდეგ ქულებს:

#     • 90-100: - A

#     • 70-89: - B

#     • 50-69: - C

#     • 0-49: - F


def student_grade(grade):
    if 90 <= grade <= 100:
         print("A")
    elif 70 <= grade <= 89:
        print("B")
    elif 50 <= grade  <= 69:
        print("C")
    else:
        print("F")
        
        
student_grade(73)