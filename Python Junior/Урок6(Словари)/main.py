# ключ(уникальное) : значения(может повторяться)
my_dict = {}
my_dict2 = {"10UA778": "Toyota", "90ZH990": "Merc", "99HZ199": "BMW", "90KF772": "Honda", "67QZ067": "Mazda", "99AA999": "Jiquli", "77BC700": "AITO", "35AC359": "Audi"}
print(my_dict2["10UA778"]) # изменение значения(машины) существующего номера
my_dict2["10UA778"] = "Lexus"
print(my_dict2) # изменение значения(машины) несуществующего номера(добавление)
my_dict2["99HU959"] = "Ford"
print(my_dict2)


my_dict = {}
# добавление одного значения для нескольких ключей
my_dict = dict.fromkeys(("99AA999", "67SS067", "99AF656", "67KK007"), "BMW") 
print(my_dict)
my_dict2 = (dict.fromkeys(("10AA123", "27PA390"), "Lexus"))
print(my_dict | my_dict2) # объединение(комбинация)


print(my_dict.keys()) # достаем ключи
print(my_dict.values()) # достаем значения
print(my_dict.items()) # достаем элемента(ключ : значения)


my_dict = {"10UA778": "Toyota", "90ZH990": "Merc", "99HZ199": "BMW", "90KF772": "Honda", "67QZ067": "Mazda", "99AA999": "Jiquli", "77BC700": "AITO", "35AC359": "Audi"}
print(my_dict["94II001"]) # выдаст ошибку ключа
print(my_dict.get("94II001")) # вернет пустоту(None)
print(my_dict)
print(my_dict.setdefault("94II001")) # создаст элемент с указанным ключом и значением пустоты(None)
print(my_dict)


my_dict = {"10UA778": "Toyota", "90ZH990": "Merc", "99HZ199": "BMW", "90KF772": "Honda", "67QZ067": "Mazda", "99AA999": "Jiquli", "77BC700": "AITO", "35AC359": "Audi"}
print(my_dict)
print(my_dict.pop("10UA778")) # удаляет по ключу
print(my_dict)
print(my_dict.popitem()) # удаляет с конца
print(my_dict)