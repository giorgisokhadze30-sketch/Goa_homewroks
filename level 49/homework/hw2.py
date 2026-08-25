# 3) მოცემულია სია celsius = [0, 25, 100, -10, 37]
# გადააქციეთ Celsius-ები Kelvin-ში map-ის გამოყენებით.# Hint: ფორმულა Kelvin = Celsius + 273

celsius = [0, 25, 100, -10, 37]

kelvin = list(map(lambda c: c + 273, celsius))

print(kelvin)