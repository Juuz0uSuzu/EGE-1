# Пользователь вводит текст (несколько строк). Найдите слово, которое встречается чаще всего
# (без учёта регистра и знаков препинания). При равном количестве вхождения слов берётся первое по счёту слово.
# Это задача 16 из прошлой темы, поднятая с уровня символов на уровень слов
# — и здесь выстраивается настоящий конвейер обработки текста.
# Входные данные:
# Язык программирования Python. Это не просто Python
# Выходные данные:
# Самое частое слово:python - 2 раз(а)

# text = input()
#
# text_lower = text.lower()
#
# for symbol in ".,!?;:-()":
#     text_lower = text_lower.replace(symbol, " ")
# st1 = text_lower.split()
# print(st1)
#
# res1=0
# res2 =''
# for i in st1:
#     res = st1.count(i)
#     if res > res1:
#         res1=res
#         res2 = i
#
# print(res1, res2)

# s = [1, 2, 3, 4, 5]
#for i in range(len(s)):
#   s[i] += 1
#print(s)

#len - возвращает кол-во элементов
#in / not in - оператор принадлежности
#+ - конктанация
#index(element) -> индекс элемент
#.append() - добавление элемента в конец списка
#.extend() - добавляет каждый элемент отдельно
#.insert() - вставляет в нужный индекс и расширяет
#.remove() - удаляет элемент по значению
#.pop() - удаляет по индексу
#.clear() - очищает список
#my_list.sort(reverse=True)
#my_list = my_list[::-1]
#my_list.reverse()
#my_list = ["beta", "alpha", "gkmma", "gamma", "omega"]

#
# pos=0
# neg=0
# nums = [1, -2, 3, -4, 5, -6, 7, -8, 9]
# for i in nums:
#     if i >= 0:
#         pos += 1
#     elif i < 0:
#         neg += 1
# print(pos, neg)

# s=[]
# for i in range(5):
#     text=input()
#     s.append(text)
# print(s)

# nums = [1, 2, 3, 2, 4, 2, 5]
#
# count = 0
# index = -1
#
# for i in range(len(nums)):
#     if nums[i] == 2:
#         count += 1
#         if count == 2:
#             index = i
#             break
#
# print(index)

# index()
# first = nums.index(2)
# nums = nums [first + 1:]
# print(nums.index(2) + first + 1)
#





