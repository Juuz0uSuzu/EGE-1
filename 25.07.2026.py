#len() min() max() in sum()
# from dataclasses import replace
# from glob import translate

#capitalize() - предложение с большой буквы
#title() - все слова с большой буквы
#upper() - все символы большие
#lower - все символы маленькие

#методы поиска
#find(a) -> hahahahaha выдаёт индекс первого символа 'a'
#index(element) -> ошибка, если элемента нет
#rfind(element) - тот же файнд, но ищет слева

#методы проверки символов
#isupper()
#islower()
#isdigit() -> проверяет цифра ли наша строка "123"
#"".isnumeric() -> более шиокий спектр проверок на число
#isallnum() -> проверяет если в строке лишь циферки, возвращает False, если находит всякий мусор
#split() -> разделяет строку по пробелу(умолчание) и возвращает список, но можно выбирать свои разделители


# s='hello,world,hello'.split(',')
# print(":".join(s))

#удаление и замена
# .strip
# .rstrip
# .lstrip
# s='helloo'
# print(s.strip('o'))
# s.replace('o', 1)
# print(s.replace('o', '1', count=1))
#hell1o]
#удалить символ можно с той же .replace используя пустой символ

#count
# s='hhhooo999nnn'
# print(s.count('h', 2 , 10))

#translate()
#print(ord("A"), ord('a'))

# my_string='hello world, My name'
# table = {
#     ord("a"): ord("@"),
#     ord("e"): ord("3"),
#     ord("M"): None,
#     ord("o"): '',
# }
# result = my_string.translate(table)
# print(result)

# my_string='hello world, My name'
# result = my_string.translate(str.maketrans('aeM', '@30', 'M'))
# print(result)

# s='***helloool***'
# # h= s[0]+s[1]+s[2]
# h=''
# for i in range(3):
#     h += s[i]
# print(h)

# start - от куда
# end - до куда (невключительно)
# step - с каким шагом

# s='***helloool***'
# print(s[0:3])
# print(s[::-1]) - переворот в обратную сторону



# string=input()
# print(string[-4:])

# string=input()
# print(string[1:-1])

# string=input()
# print(string[:5] + string[-5:])

# string=input()
# s=string[::-1]
# print(s[:5])
# print(string[-5:][::-1])

# s=input()
# mid=len(s)//2
# print(s[mid:]+s[:mid])

# s=input()
#
# for i in range(len(s)-2):
#     a=s[i:i+3]
#     print(a)


# s= 'шалаш, камыш, заказ, возврат, довод'
# a=(s.split(', '))
# for i in range(len(a)):
#     if a[i] == a[i][::-1]:
#         print(a[i])

# s='hoooohhoodaooooa'
# a=''
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         sub= s[i:j]
#         if sub == sub[::-1] and len(sub) > len(a):
#             a=sub
# print(a, len(a))





















































