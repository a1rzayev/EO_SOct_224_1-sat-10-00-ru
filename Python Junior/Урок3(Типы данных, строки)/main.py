# узнаем тип переменной
print(type("Sanan"))

# сравниваем два текста
print(type("Mikayil" == "Muhammed"))

# строки 
hello = "Hello world"
print("Length of string: ", len(hello))

# операции со строками
hello = "Hello"
world = "World!"
print(hello + world) # сумма

print(hello, world) # связной

print(world * 3) # умножение

string = "Privet mir!"

# разделение по символу
string_list = string.split()
print(string_list)

string_1 = "Privet Farid, kak dela?"
print("lower:", string_1.lower()) # весь текст нижним шрифтом
print("upper:", string_1.upper()) # весь текст большим шрифтом
print("title:", string_1.title()) # заглавная буква каждого элемента большим шрифтом
print("capitalize:", string_1.capitalize()) # заглавная буква предложения(всего текста) большим 
print("swapcase:", string_1.swapcase()) #  меняет больой шрифт на маленький и обратно