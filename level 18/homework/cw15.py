# 16) შექმენით ფუნქცია და არგუმენტად გადაეცით String-ი. ფუნქციამ უნდა "გაფილტროს" ეს სტრინგი თანხმოვანი ასოებისგან 
# და მხოლოდ დააბრუნოს ის ხმოვანი ასოები, რომლებსაც ეს სტრინგი შეიცავს.




def filter_vowels(text):
  vowels = "aeiouAEIOU"
  result = ""

  for i in text:
    if i in vowels:
      result +=i
  return result

print(filter_vowels("GIOrgi"))
