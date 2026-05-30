from random import randint # импортируем библиотеку


problem_list = ["Living Giant Tree", "Alien Flying Saucer",
                "Monster Spirit from the Parallel Universe",
                "Evil Artificial Intelligence", "Parasites That Capture the Brain",
                "Mutant Centipede", "Mad Godzilla", "Black Dragon", "Titanium"] # список проблем

problem = problem_list[randint(0, len(problem_list) - 1)] # рандомно генерируем 0 до конечного индекса
print("The problem is:", problem) # выводим проблему
list_of_heroes = [input(), input(), input()] # тройной ввод для супергероев
print("These Superheroes:", list_of_heroes, "went on a mission") # показать, что они вышли на миссию
