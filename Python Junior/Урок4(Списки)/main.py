list = ["Sadiq", "Atilla", "Senan", "Camal", "Mikayil", "Ferid", "Muhammed"] # список
print(list)
print(len(list)) # длина списка

list.append(10) # добавление элемента в список
print(list)
print(len(list))

name = "Good day"
list.append(name) # добавление элемента в список
print(list)
print(len(list))

student = "Muhammed"
list.insert(1, "student") # вставить элемент по индексу
print(list)
print(len(list))

list.reverse() # отзеркалить список
print(list)
print(len(list))

print(list[0][:4]) # распечатать до 4-го элемента из первого элемента

#[начальный_индекс(включительно) : конечный_индекс(невключительно) : шаг]

print(list.index(10)) # разпечатать индекс какого-то элемента из списка

list.pop(1) # удаляет элемент по индексу(если не указать, удалит последнее)

list.remove("student") # удаляет по названию


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#[начальный_индекс(включительно) : конечный_индекс(невключительно) : шаг]
print(numbers[::2])




