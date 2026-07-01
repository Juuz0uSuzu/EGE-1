# Пользователь вводит температуру и единицу измерения: C (Цельсий)
# или F (Фаренгейт). Программа конвертирует значение в другую
# шкалу и выводит результат с округлением до 1 знака после запятой.
# Формулы:
# из C в F: F = C * 9/5 + 32
# из F в C: C = (F - 32) * 5/9
# Если введена неверная единица — выведи ошибку.
#
# temp=float(input("Enter temperature: "))
# type=str(input("Enter the type of temperature: "))
# match type:
#     case "C":
#         result=temp*9/5+32
#         print(round(result))
#     case "F":
#         result=(temp-32)*5/9
#         print(round(result))
#     case _:
#         print("Invalid input")
#
#
# Пользователь вводит сумму покупки и количество накопленных бонусных баллов. Правила:
# базовая скидка: 5% при сумме от 5000 ₽, 10% — от 10 000 ₽;
# дополнительно: за каждые 100 баллов можно списать 1% от итоговой суммы
# (но не более 20% суммарной скидки);
# баллы списываются только если их достаточно для получения хотя бы 1% скидки.
# Выведи: итоговую сумму к оплате, сколько баллов списано, итоговый процент скидки.
#
# total=float(input())
# bonuses=int(input())
# if 5000<=total<10000:
#     total=total*0.95
#     if bonuses>=100:
#         celoe=bonuses//100
#         if celoe>20:
#             celoe=20
#             print(total*(1-(celoe/100)), celoe*100, celoe)
#
#
# summ = float(input())
# bonus = int(input())
# price = summ
# if 5000 <= summ < 10000:
#     price = summ * 0.95
# elif 10000 <= summ:
#     price = summ * 0.9
# balls = bonus // 100
# if balls > 20:
#     balls = 20
# print(price * (1 - (balls / 100)), balls * 100, balls)

#
# s='hello world'
# s1=[1,2,3,4,5]
# s2=(1,2,3,4,5)
# print(s1[4])
# print(s1[-1])
# print(s[len(s)-1])
# print(len(s)) # метод получения длинны итерируемого обьекта
# print(len(s1))

#sum(s1) - складывает элементы
#min(s1) - нахождение минимального элемента
#max(s1) - нахождение максимального элемента
#print(a)
#abs() - модуль
#
# while условие:
#     тело цикла
#
# a=0
# while a<10:
#     a+=1
#     if a==5:
#         print('xxx')
#
# print(a)

#continue - останавливает текущую операцию и возвращается в начало цикла
#break - останавливает исполнение цикла
#
#
# num=88
# while True:
#     user=int(input())
#     if user < num:
#         print('число больше')
#     elif user > num:
#         print('число меньше')
#     else:
#         print('угадал')




























