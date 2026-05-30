from turtle import * #подключили все функции с библиотеки

shape("turtle") #указываем форму нашей кисти

pensize(3) #размер кисти
color("red", "green") # цвета: 1) кисти, 2) черепашки

penup() #поднимаем кисть(не пишет)
pendown() #опускаем кисть(пишет)

forward_index = int(input("введите длину движения вперед: "))
turn_index = int(input("введите угол поворота: "))

forward(forward_index) #движение вперед
left(turn_index) #поворот налево
forward(forward_index) #движение вперед
left(turn_index) #поворот налево
forward(150) #движение вперед
left(turn_index) #поворот налево
forward(150) #движение вперед

pensize(10) #размер кисти
color("blue", "black") # цвета: 1) кисти, 2) черепашки

begin_fill() #начать заливку(заливка будет в цвете черепашки, а не кисти)
circle(75) #нарисовать круг с радиусом 
end_fill() #закончить заливку
