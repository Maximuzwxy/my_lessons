# # 12.12
# lst = [10, 24, 53, 47, 45, 78, 20, 70, 81, 7]
# lst1 = []
#
# while lst:
#     min_index = 0
#     for i in range(len(lst)):
#         if lst[min_index] > lst[i]:
#             min_index = i
#     lst1.append(lst.pop(min_index))
# print(lst)
# print(lst1)
#
# s = input('s: ')
# sep = input('sep: ')
#
# lst = list(s)
# print(lst)
#
# ss = ''
# for i in range(len(lst) - 1):
#     ss += lst[i] + sep
# ss += lst[-1]
# print(ss)
#
#
import random
lst1 = random.sample(range(100), 6)
lst2 = random.sample(range(100), 8)
lst1.append(201)
lst1.append(170)
print(lst1)
print(lst2)

lst= []

while lst1 and lst2:
    min1 = min(lst1)
    min2 = min(lst2)

    if min1 <= min2:
        lst.append(min1)
        lst1.remove(min1)
    else:
        lst.append(min2)
        lst2.remove(min2)

while lst1:
    a = min(lst1)
    lst.append(a)
    lst1.remove(a)

while lst2:
    a = min(lst2)
    lst.append(a)
    lst1.remove(a)

print(len(lst))
print(lst)

