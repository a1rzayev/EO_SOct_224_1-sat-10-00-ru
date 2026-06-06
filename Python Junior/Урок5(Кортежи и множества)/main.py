# разница между списком и 
numbers_list = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5]
numbers_set = {1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5}
print(numbers_list)
print(numbers_set)


# проверяем есть ли элемент Х в множестве
our_set = set()
our_set2 = {0}
x = "tomato"
our_set.add("tomato")
our_set2.add("potato")
print(x in our_set)
print(x in our_set2)


# проверяем есть ли общие элементы
our_set = {1, 2, 3, 4, 5}
our_set2 = {5, 6, 7, 8, 9}
print(our_set.isdisjoint(our_set2))


# функции объединения и обновления
our_set1 = {1, 2, 3, 4, 5}
our_set2 = {5, 6, 7, 8, 9}
our_set3 = {}
print("our_set1:", our_set1)
print("our_set2:", our_set2)
print("our_set3:", our_set3) 
our_set2.union(our_set1)
print("our_set1:", our_set1)
print("our_set2:", our_set2)
print("our_set3:", our_set3) 
our_set2.update(our_set1)
print("our_set1:", our_set1)
print("our_set2:", our_set2)
print("our_set3:", our_set3) 


# найти подмножество и надмножество
our_set1 = {1, 2, 3}
our_set2 = {4, 5, 6}
our_set3 = {1, 2, 3, 4, 5}
print(our_set1.issubset(our_set3))
print(our_set2.issubset(our_set3))
print(our_set3.issuperset(our_set1))
print(our_set3.issuperset(our_set2))