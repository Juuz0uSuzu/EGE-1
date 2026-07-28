# 1.
# Пользователь вводит строку.
# Напишите программу, которая выводит поочерёдно:
#
# Символ, который встречается в строке чаще всего и количество его вхождений
# Каждый третий символ
# Самую длинную подстроку, расположенную между двумя повторяющимися символами

# text = input("Введите строку: ")
#
# counts = {}
# for char in text:
#     if char in counts:
#         counts[char] += 1
#     else:
#         counts[char] = 1
#
# max_char = text[0]
# for char in counts:
#     if counts[char] > counts[max_char]:
#         max_char = char
#
# print(max_char, counts[max_char])
#
# print(text[2::3])

# 2.
# ```
# Пользователь вводит строку и число n. Реализуйте циклический сдвиг строки влево на n символов.
# Те символы, что "ушли" влево, должны появиться справа.
# Входные данные:
# abcdef
# Выходные данные:
# cdefab
#
# ```

# s = input("Введите строку: ")
# n = int(input("Введите число: "))
#
# n = n % len(s)
#
# result = ""
#
# for i in range(n, len(s)):
#     result = result + s[i]
#
# for i in range(0, n):
#     result = result + s[i]
#
# print(result)