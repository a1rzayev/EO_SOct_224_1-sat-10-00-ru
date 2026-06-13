age = "12"
print(age * 2) # age - текст(string)
age = int(age) # преобразуем str -> int
print(age * 2) # age - целое число(int)


age = "Cafar" # не сработает(имя не может стать числом)
print(age * 2)
age = int(age)
print(age * 2)


age = "11.7"
print(age * 2) # age - текст(string)
age = float(age) # преобразуем str -> float
print(age * 2) # age - число(float)


# любой тип данных можно преобразовать, если не выдает ошибку и соответствует