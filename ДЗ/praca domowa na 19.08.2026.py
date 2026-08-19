# 1. Создайте программу, которая анализирует текст:
# Принимает две строки от пользователя.
# Создает множества из букв каждой строки (без пробелов и знаков препинания).
# Находит общие буквы, уникальные буквы первой строки, уникальные буквы второй строки.
# Определяет, какая строка содержит больше уникальных букв.
#
# text1 = input()
# text2 = input()
#
# text1 = text1.replace(" ", "")
# text2 = text2.replace(" ", "")
#
# set1 = set(text1.lower())
# set2 = set(text2.lower())
#
# common = set1 & set2
# unique1 = set1 - set2
# unique2 = set2 - set1
#
# print(common)
# print(unique1)
# print(unique2)
#
# if len(unique1) > len(unique2):
#     result = "В первой строке больше уникальных букв"
# elif len(unique1) < len(unique2):
#     result = "Во второй строке больше уникальных букв"
# else:
#     result = "Количество уникальных букв одинаково"
# print(result)


# 2. У вас есть три множества участников книжного клуба, читающих разные жанры книг:
# fantasy_readers = {"Игорь", "Катя", "Лев", "Марина"}
# detective_readers = {"Катя", "Лев", "Никита", "Ольга"}
# sci_fi_readers = {"Лев", "Марина", "Никита", "Павел"}
# Найдите:
# Участников, которые читают книги всех трёх жанров.
# Участников, которые читают только фантастику.
# Участников, которые читают ровно два жанра
#

# fantasy_readers = {"Игорь", "Катя", "Лев", "Марина"}
# detective_readers = {"Катя", "Лев", "Никита", "Ольга"}
# sci_fi_readers = {"Лев", "Марина", "Никита", "Павел"}
# a = fantasy_readers & detective_readers & sci_fi_readers
# b = fantasy_readers - detective_readers - sci_fi_readers
# c = ((fantasy_readers & detective_readers) | (fantasy_readers & sci_fi_readers) | (detective_readers & sci_fi_readers)) - a
# print(a, b, c, sep='      ')


# 3.В школе есть три множества учеников, занимающихся разными видами спорта:
# football_players = {"Алексей", "Богдан", "Вика", "Дарья"}
# basketball_players = {"Богдан", "Вика", "Егор", "Зоя"}
# volleyball_players = {"Вика", "Дарья", "Егор", "Ирина"}
# Найдите:
# Всех учеников, которые занимаются хотя бы одним видом спорта.
# Учеников, которые занимаются ровно одним видом спорта.
# Учеников, которые занимаются волейболом, но не занимаются баскетболом.
#

# football_players = {"Алексей", "Богдан", "Вика", "Дарья"}
# basketball_players = {"Богдан", "Вика", "Егор", "Зоя"}
# volleyball_players = {"Вика", "Дарья", "Егор", "Ирина"}
#
# a = football_players | basketball_players | volleyball_players
# b = (football_players - basketball_players - volleyball_players) | (basketball_players - football_players - volleyball_players) | (volleyball_players - football_players - basketball_players)
# c = volleyball_players - basketball_players
# print(a, b, c, sep='      ')





# 4.В языковой школе есть три множества студентов, изучающих разные языки:
# english_students = {"Михаил", "Наташа", "Олег", "Полина"}
# spanish_students = {"Наташа", "Олег", "Роман", "Света"}
# french_students = {"Олег", "Полина", "Роман", "Татьяна"}
# Создайте множество всех студентов и добавьте нового студента "Антон" в группу английского языка.
# Найдите студентов, которые изучают только один язык, с помощью итерации по множествам.
# Удалите студента "Олег" из всех групп.

# english_students = {"Михаил", "Наташа", "Олег", "Полина"}
# spanish_students = {"Наташа", "Олег", "Роман", "Света"}
# french_students = {"Олег", "Полина", "Роман", "Татьяна"}
#
# english_students.add("Антон")
# all_students = english_students | spanish_students | french_students
# only_one_lang = (english_students - spanish_students - french_students) | (spanish_students - english_students - french_students) | (french_students - english_students - spanish_students)
# english_students.discard("Олег")
# spanish_students.discard("Олег") #дискриминация олегов
# french_students.discard("Олег")
#
# print(english_students, spanish_students, french_students)
# print(only_one_lang)