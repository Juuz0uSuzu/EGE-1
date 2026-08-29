# В журнале посещаемости пропуск отмечен символом "-", а присутствие — "+".
# Напишите функцию max_streak(data, value), которая принимает список и искомое значение
# и возвращает кортеж из длины самой длинной серии подряд идущих таких значений и индекса её начала.
# Если значение в списке не встречается, функция возвращает строку "Значение не найдено".
# Примеры вызова:
# max_streak(['+', '-', '-', '+', '-', '-', '-', '+'], '-') -> (3, 4)
# max_streak([1, 1, 2, 1], 1) -> (2, 0)
# max_streak([1, 2, 3], 5) -> 'Значение не найдено'
#
#
# def max_streak(data, value):
#     if value not in data:
#         return 'Значение не найдено'
#
#     max_length=0
#     max_start=0
#     current_length=0
#     current_start=0
#
#     for i in range(len(data)):
#         if data[i] == value:
#             if current_length == 0:
#                 current_start = i
#             current_length +=1
#         else:
#             if current_length > max_length:
#                 max_length = current_length
#                 max_start = current_start
#             current_length = 0
#
#     if current_length > max_length:
#         current_length = max_length
#         max_start = current_start
#
#     return (max_length, max_start)
#
# print(max_streak(['+', '-', '-', '+', '-', '-', '-', '+'], '-'))
# print(max_streak([1, 1, 2, 1], 1))
# print(max_streak([1, 2, 3], 5))


# Напишите функцию to_binary(n, width=8), которая принимает неотрицательное целое число
# и возвращает строку с его двоичной записью, дополненную слева нулями до длины width (по умолчанию 8).
# Если двоичная запись длиннее width, она возвращается целиком.
# Для отрицательного числа функция возвращает строку "Только неотрицательные числа".
# Примеры вызова:
# to_binary(5) -> '00000101'
# to_binary(10, 4) -> '1010'
# to_binary(0) -> '00000000'
# to_binary(-3) -> 'Только неотрицательные числа'
#
#

# def to_binary(n, width=8):
#     if n < 0:
#         return "Только неотрицательные числа"
#
#     binary = bin(n)[2:]
#     if n == 0:
#         binary = "0"
#
#     if len(binary) < width:
#         binary = "0" * (width - len(binary)) + binary
#
#     return binary
#
# print(to_binary(5))
# print(to_binary(10, 4))
# print(to_binary(0))
# print(to_binary(-3))

# Телефон вчера видел один набор Wi-Fi сетей, а сегодня другой. Напишите функцию
# compare_networks(yesterday, today), которая принимает два множества
# и возвращает кортеж из двух множеств: появившиеся сети и пропавшие.
# Если наборы полностью совпадают, функция возвращает строку "Изменений нет".
# Примеры вызова:
# compare_networks({'home', 'guest'}, {'home', 'cafe'}) -> ({'cafe'}, {'guest'})
# compare_networks({'home'}, {'home'}) -> 'Изменений нет'
# compare_networks({'home', 'guest'}, {'home'}) -> (set(), {'guest'})

# def compare_networks(yesterday, today):
#     if yesterday == today:
#         return 'Изменений нет'
#
#     appeared = today - yesterday
#     disappeared = yesterday - today
#     return (appeared, disappeared)
#
# print(compare_networks({'home', 'guest'}, {'home', 'cafe'}))
# print(compare_networks({'home'}, {'home'}))
# print(compare_networks({'home', 'guest'}, {'home'}))

