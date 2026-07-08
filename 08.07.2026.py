# s = [1,2,3,4,5,6,7,8,9,10]
# d="hello world"
# for element in d:
#     print(element)
from asyncio import ensure_future

#start - начало последовательности
#stop - конец последовательности (не включительно)
#step - интервал между элементами последовательности
#s = range(start, stop, step)

# s = list(range(100))
# for i in s:
#     print(i)

# for i in range(100):
#     print(i)

# s = "hello world"
# for i in range(5):
#     print(s[i])

# for i in range(10,1, -2):
#     print(i)

# for i in range(1, 3):
#     print("Значение внешнего цикла", i)
#     for j in range(1, 3):
#         print("Значение внутреннего цикла", j)
#     print()

# for i in range(1, 5):
#     for j in range(1, 5):
#         print(i,'*',j,'=',i*j)
#     print()

# i = 1
# while i < 5:
#     j = 1
#     while j < 5:
#         print(i, '*', j, '=', i * j)
#         j += 1
#     print()
#     i += 1

# for i in range(5, 0, -1):
#     print('*' * i)

# for i in range(5, 0, -1):
#      for j in range(i):
#          print('*', end='')
#      print()

# for i in range(5, 0 ,-1):
#     s=''
#     for j in range(i):
#         s+='*'
#     print(s)

# print('hello', 'world', sep='', end='')
# print('123')
#
# n=5
# for i in range(n):
#     print(" " * (n - i - 1), "#" * (2*i+1), sep="")

