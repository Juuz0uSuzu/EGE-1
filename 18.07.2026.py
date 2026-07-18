# import math
# serial_num_len=105
# nums=65536
# memory_size=7 * 2 ** 20
# for alpabet in range(1, 10000):
#     bits = math.ceil(math.log2(alpabet))
#     bytes = math.ceil(bits * serial_num_len / 8)
#     if bytes * nums > memory_size:
#         print(alpabet)
#         break
from itertools import count

#14

# num=int(input())
# count=0
# while num:
#     a=num%10
#     if a <=5:
#         count +=1
#     num//=10
# print(count)

# num=input()
# count=0
# for i in num:
#     if int(i)<=5:
#         count+=1
# print(count)



# Определите количество цифр с числовым значением, превышающим 8
# num=4*3125**2019+3*625**2020-2*125**2021+25*2022-4*5**2023-2024
# count=0
# while num:
#     if num%10>8:
#         count+=1
#     num=num//10
# print(count)


# num=4*3125**2019+3*625**2020-2*125**2021+25*2022-4*5**2023-2024
# count=0
# while num:
#     if num%25>10:
#         count+=1
#     num=num//25
# print(count)

# num=4*25**2022-2*5**2000+125**1011-3*5**100-660
#
# count=0
# while num:
#     if num % 5 == 4:
#         count+=1
#     num=num//5
# print(count)

# num=1331**650-55*121**610+77*11**510-3*11**100-221
# count=0
# while num:
#     if num%11==10:
#         count+=1
#     num=num//11
# print(count)

# num=(16**350*(15*3-29)**(4**(2+5))+1007)//63
# print(num)
# count=0
# while num:
#     if num %4 == 1:
#         count+=1
#     num=num//4
# print(count)


# num=(16**350*(15*3-29)**(4**(2+5))+1007)//63
# # 4
# s=""
# while num:
#     s+=str(num%4)
#     num //=4
# print(s)

# num=4*644+4**322+16**35-64**3
# count=0
# while num:
#     if num%4==3:
#         count+=1
#     num=num//4
# print(count)

# num = (16**350*(15*3-29)**(4**(2+5))+1007)//63
# # 4
# s = ""
# while num:
#    s += str(num % 4)
#    num //= 4
#
# print(s.count("1"))

# s='hello world'
# # print(s[0], s[1])
# # print(s[-1])
# for char in s:
#     print(char, end=' ')

s="'hello'\"world\""
s="hello\\world"
s="hello\nworld"
s="hello\tworld"
s=r"hello\tworld"
print(s)