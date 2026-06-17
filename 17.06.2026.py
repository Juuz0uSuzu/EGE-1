

#name = True
#name2 = False
#
#print({} != {})

# == и != работают для всех типов данных

#print((1, 2, 3) == [1, 2, 3]) #сравнение разных типов данных всегда будет давать False
#print(1.1>1) # исключение - числовые типы
#  == < > >= <= !=
#print(10>3) # результат сравнения всегда bool

# аналог " == "

#num1 = 10
#num2 = 20
#print(num1 is num2)

# Оператор " is " проверяет наличие хранения переменной в ячейке

#str1=('hello')
#str2=(2, 35, 6)
#print("ll" in str1)
#print(2 in str2)

# Оператор " in " - оператор принадлежности


#not in
#str1="hello"
#print("ll" not in str1)
#print(not("ll" in str1))
#not - оператор отрицания


#and or not

#print(True and False) # одна ложь - ложь везде
#0 0 0
#1 0 0
#0 1 0
#1 1 1
#print(True or False) #одна истина - истина везде
#0 0 0
#1 0 1
#0 1 1
#1 1 1

#not
#0 -> 1
#1 -> 0

#импликация
#A -> B  ==  A<=B

#  <=

#0 <= 0  1
#0 <= 1  1
#1 <= 0  0
#1 <= 1  1

#a=False
#b=True
#print(a <= b)

#эквивалентность

# ==

#0 0 1
#1 0 0
#0 1 0
#1 1 1

#исключающее или
# (+)
# ^

#0 0 0
#0 1 1
#1 0 1
#1 1 0

#a=True
#b=False
#print(a ^ b)
#print((a or b) and (a!=b))



#Стрелка пирса ( or наоборот )

#a=True
#b=False
#print(not(a or b))

#0 0 1
#0 1 0
#1 0 0
#1 1 0


#Штрих Шеффера

# A|B

#not(A and B)

#0 0 1
#0 1 1
#1 0 1
#1 1 0

# алгебра логики
# 1 - ()
# 2 - not
# 3 - and
# 4 - or
# 5 - <= (->)
# 6 - эквивалентность


# В Python
# 1 -  ()
# 2 -  (**)
# 3 -  (/, *, //, %)
# 4 -  (+-)
# 5 -  (>, <, >=,<=, ==, !=)
# 6 -  not
# 7 -  and
# 8 -  or





#a = '123A3A'
#int(строка, система счисления[2-36])
#print(int(a, 16))
#print(format(20, 'b'))
#b-2
#o-8
#x-16
#print(f"{20, "b"))
#двоичное представление числа
#a=5
#print(bin(a))

#восьмеричное представление числа
#print(oct(5))


#шестнадцатеричное представление числа
#print(hex(29))

#import название
import math
#print(math.log10(100)) # в какую степень основания чтобы получить X
#корень
#print(math.sqrt(100))
#print(100**(1/2))

#округление

# до меньшего
#a=10.7
#print(int(a), a//1)
#print(math.floor(a))

# до большего
#print(math.ceil(a))

#округление по математическим правилам
#print(round(a))

# x= True
# y= True
# z= False
# w= True
# (x == y) or (z <= w)
# (1) or (0<=1)
# 1 or 1
# print(True or True)

#x=True
#y=False
#z=False
#w=True
#(x==y) or ((y or z) <= x)
#print((x==y) or ((y or z) <= x))
# (0) or ((0 or 0) <= 1)
# n1, n2, n3 = 10, 15, 17
# step1=(n1 *(n3-n2))
# step2=n2**2
# step3=n3%3+step1
# result= oct(step3//step2)
# print(result)
#4*x+1B_16-67_8=0
#print(int("1B", 16))
#27
#print(int("67", 8))
#55
# x=(-int('1B', 16) +int('67', 8)) / 4
# print(x)
