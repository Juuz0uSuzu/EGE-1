#Программа принимает на вход сумму дохода сотрудника за год.
#Налог рассчитывается по прогрессивной шкале с условиями:До 100 000 — налог 0%.От 100 001 до 500 000 — налог 10% на сумму,
#превышающую 100 000.От 500 001 до 1 000 000 — фиксированно 40 000 + 15% на сумму,
#превышающую 500 000.Свыше 1 000 000 — фиксированно 115 000 + 20% на сумму, превышающую 1 000 000.
#Дополнительно: если у сотрудника есть статус резидента (вводится строка "да"/"нет"),
#итоговый налог уменьшается на 5% (умножается на 0.95), но только если доход не превышает 1 000 000.
#
#wage = float(input('Введите ваш доход: '))
#resident = input("У вас есть статус резидента? (да/нет): ")
#
#if wage <= 100000:
#    tax = 0
#elif wage <= 500000:
#    tax = (wage - 100000) * 0.10
#elif wage <= 1000000:
#    tax = 40000 + (wage - 500000) * 0.15
#else:
#    tax = 115000 + (wage - 1000000) * 0.20
#
#if resident == "да" and wage <= 1000000:
#    tax = tax * 0.95
#
#print(f"Сумма налога: {tax:.2f}")


#На вход подается целое число от 1 до 100 включительно.
#Программа должна вывести его римское представление (например: 4 -> IV, 49 -> XLIX, 99 -> XCIX).

#n = int(input())

#hundreds = (n % 1000) // 100
#tens = (n % 100) // 10
#ones = n % 10
#
#result = ""
#
#match hundreds:
#    case 1: result += "C"
#    case 2: result += "CC"
#    case 3: result += "CCC"
#    case 4: result += "CD"
#    case 5: result += "D"
#    case 6: result += "DC"
#    case 7: result += "DCC"
#    case 8: result += "DCCC"
#    case 9: result += "CM"

#match tens:
#    case 1: result += "X"
#    case 2: result += "XX"
#    case 3: result += "XXX"
#    case 4: result += "XL"
#    case 5: result += "L"
#    case 6: result += "LX"
#    case 7: result += "LXX"
#    case 8: result += "LXXX"
#    case 9: result += "XC"
#
#match ones:
#    case 1: result += "I"
#    case 2: result += "II"
#    case 3: result += "III"
#    case 4: result += "IV"
#    case 5: result += "V"
#    case 6: result += "VI"
#    case 7: result += "VII"
#   case 8: result += "VIII"
#    case 9: result += "IX"
#
#print(result)

#На вход подаются шесть чисел: координаты центра и радиус первой окружности (x1, y1, r1),
#а затем координаты центра и радиус второй окружности (x2, y2, r2).
#Определите их взаимное расположение.Возможные ответы: «Не пересекаются (снаружи)»,
#«Не пересекаются (одна внутри другой)», «Касаются снаружи», «Касаются изнутри», «Пересекаются в двух точках», «Совпадают».

x1=float(input())
y1=float(input())
r1=float(input())
x2=float(input())
y2=float(input())
r2=float(input())

if x1=x2 and y1=y2 and r1=r2:
    print('Совпадают')
elif 








