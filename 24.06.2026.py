# num=int(input())
#
# a=num//100
# b=(num//10)%10
# c=num%10
#
# count=0
# if a%2==0 or a%5==0:
#     count+=1
# if b%2==0 or b%5==0:
#     count+=1
# if c%2==0 or c%5==0:
#     count+=1
# if count>=2:
#     print(num)
# else:
#     print(num+1)


#Напишите программу, для вычисления корней квадратного уравнения вида: ax2+bx+c=0, которая принимает от пользователя значения коэффициентов a, b и c, причем с проверкой условия: a≠0.
#Для извлечения корня воспользуйтесь функцией sqrt модуля math.
# import math
# a=float(input())
# b=float(input())
# c=float(input())
# if a==0:
#     print("Ошибочка")
# else:
#     D=b**2-4*a*c
#     if D<0:
#         print("Корней нема")
#     elif D==0:
#         x=-b/(2*a)
#         print(x)
#     else:
#         x1= (-b+math.sqrt(D))/(2*a)
#         x2= (-b-math.sqrt(D))/(2*a)
#         print(x1,x2)







# match <выражение>:
#     case <шаблон 1>:
#         <действие 1>
#     case _:
#          <действие по умолчанию>
# value=int(input())
# match value:
#     case 3:
#         print(value)
#     case 1|5:
#         print(value+1)
#     case _:
#         print("Чёт другое")
# | = или
# _ = все остальные варианты
#
# value=int(input())
# match value:
#     case x:
#         print(x)

# point=(10, 0)
# match point:
#     case (0, 0):
#         print("В начале координат")
#     case (0, y):
#         print(0, y)
#     case (x, 0):
#         print(x,  0)
#     case (x, y):
#         print('Произвольная точка', x, y)


# value=int(input())
#
# match value:
#     case x if x>0:
#         print('x-polozhit')
#     case x if x<0:
#         print('x-otricat')
#     case _:
#         print('zero')



# value = int(input())
# data= value / 10 if value > 10 else value % 10
# print(data)

# num=int(input("Введите число месяца ->  "))
# match num:
#     case 1|3|5|7|8|10|12:
#         print('31 день')
#     case 2:
#         print('28 дней')
#     case _:
#         print('30 дней')

# num=int(input("Введите возраст -->  "  ))
# match num:
#     case x  if x<7:
#         print("Дошкольник")
#     case x if 7<=x<18:
#         print("Школьник")
#     case x if 18<=x<22:
#         print("Студент")
#     case x if 22<=x<65:
#         print("Рабочий")
#     case x if x>=65:
#         print("Пенсионер")
#     case _:
#         print("Некоректный ввод")



# znak=input("Введите знак действия -->   ")
# match znak:
#     case x if '+':
#         a=float(input())
#         b=float(input())
#         print(a+b)
#     case x if '-':
#         a=float(input())
#         b=float(input())
#         print(a-b)
#     case x if '*':
#         a=float(input())
#         b=float(input())
#         print(a*b)
#     case x if '/':
#         a=float(input())
#         b=float(input())
#         print(a/b)
#     case _:
#         print('error')


# x, y=int(input()), int(input())
# match (x, y):
#     case (x, y) if x>=0 and y>0|x>0 and y>=0| x==0 and y==0:
#         print("Начало координат")
#     case (x, y) if x>0 and y>0:
#         print("Первая четверть")
#     case (x, y) if x<0 and y<0:
#         print("Третья четверть")
#     case (x, y) if x<0 and y>0:
#         print("Вторая четверть")
#     case (x, y) if x>0 and y<0:
#         print("Четвёртая четверть")
#





















