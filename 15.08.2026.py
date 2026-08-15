# list - изменяемый, индексируемый, нетипизированный набор данных
# append, extend, pop(0), clear(), sort, remove(element), count(), reverse(), insert(), index()

#str - множество символов
# s='dddddddddddsdsddsd'
# s[10]='h'
# .replace('z', 'v'),  .split(','), ' ,'.join(['world', 'obama'])


# cnt=0
# s=[1,2,3,4]
# for i in range(len(s)):
#     cnt+=s[i]
# print(cnt)
#
# sum(s)
# min(s)
# max(s)



# s={1,2,3,3,4,5,3, 'a', 'a'}
# s.add('turms')
# # print(type(s), s[1])
# # for i in s:
# #     print(i)
# s.pop() #удаляет элемент из начала
# s.remove('turms')
# d = s.copy()
# d.add('turmsek')
# print(d)
# print(len(s), s, 'turms' in s)
# s.pop()



# s = {0,2,4,5,6,8, 'a', 'a'}
# s.discard('a')
# print(s)



# s = {0,2,4,5,6,8}
# s1 = {0,1,3,5,7,9}
# # set_3 = s.union(s1)
# # z = s.union(s1)
# set_3 = s|s1
# print(set_3)
# print(z)
# print(set_3)
#
# set_4=s.intersection(set_3)
#set4= s & set_3
# print(set_4)

# set_5=s.difference(s1)
# print(set_5)
# s.difference_update(s1)
# .difference = '-'
# print(s, set_5)

# set_3=s.symmetric_difference(s1)

# symmetric_difference = ^
# print(set_3)
# s.symmetric_difference_update(set_3)
# print(s)


# small_set={3, 5, 7}
# big_set={1, 3, 5, 7, 9}
# print(small_set.issubset(big_set))
# print(small_set.issuperset(big_set))
# print(big_set.issuperset(small_set))
# print(big_set.issubset(small_set))

# Дан список fruits = ["яблоко", "банан", "яблоко", "апельсин", "банан", "киви"]
# Создайте из него множество уникальных фруктов и выведите количество уникальных элементов

# fruits = ["яблоко", "банан", "яблоко", "апельсин", "банан", "киви"]
# s=set(fruits)
# print(len(s))

# set1={1,2,3}
# set2={4,5,6}
# set3=set1.union(set2)
# print(set3)

# A={2, 4}
# B={1, 2, 3, 4, 5}
# print(A.issubset(B))
# print(A<=B)


# У вас есть три множества студентов, изучающих разные предметы:
# math_students = {"Анна", "Борис", "Вера", "Глеб"}
# physics_students = {"Борис", "Вера", "Дмитрий", "Елена"}
# chemistry_students = {"Вера", "Глеб", "Дмитрий", "Жанна"}
#
# Найдите:
# Студентов, изучающих все три предмета
# Студентов, изучающих только математику
# Студентов, изучающих математику или физику, но не химию
#
# math_students = {"Анна", "Борис", "Вера", "Глеб"}
# physics_students = {"Борис", "Вера", "Дмитрий", "Елена"}
# chemistry_students = {"Вера", "Глеб", "Дмитрий", "Жанна"}
#
# a=math_students.intersection(physics_students).intersection(chemistry_students)
# b=math_students.difference(physics_students).difference(chemistry_students)
# c=(math_students|physics_students).difference(chemistry_students)
# print(a, b, c, sep='      ')

# a=math_students& physics_students & chemistry_students
# b=math_students - physics_students - chemistry_students
# c=(math_students|physics_students) - chemistry_students
# print(a, b, c, sep='      ')

# Даны два списка:
# list1 = [1, 3, 5, 7, 9, 11, 13, 15]
# list2 = [2, 3, 6, 7, 10, 11, 14, 15]
#
# Найдите:
# Элементы, которые есть в обоих списках
# Элементы, которые есть в первом списке, но отсутствуют во втором
# Элементы, которые есть только в одном из списков (симметричная разность)

# list1 = [1, 3, 5, 7, 9, 11, 13, 15]
# list2 = [2, 3, 6, 7, 10, 11, 14, 15]
#
# l1=set(list1)
# l2=set(list2)
# a= l1 & l2
# b= l1-l2
# c= l1.symmetric_difference(l2)
# print(a, b, c)


# У вас есть множество numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}. Напишите программу, которая:
# Удаляет все четные числа из множества, используя метод discard() в цикле.
# Добавляет квадраты всех оставшихся чисел.
# Выводит итоговое множество.

# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#
# for i in numbers.copy():
#     if i % 2 == 0:
#         numbers.discard(i)
#     else:
#         numbers.add(i**2)
# print(numbers)

