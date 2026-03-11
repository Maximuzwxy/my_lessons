import math
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# for i in range(ord('A'), ord('Z') + 1):
#     if is_prime(i):
#         print(i, chr(i))
#
# for i in range(ord('a'), ord('z') + 1):
#     if is_prime(i):
#         print(i, chr(i))

def com_dict(a, b):
    s1 = a.lower()
    s2 = b.lower()

    if s1 == s2:
        return a
    else:
        len1 = len(s1)
        len2 = len(s2)

        for i in range(min(len1, len2)):
            if ord(s1[i]) < ord(s2[i]):
                return a
            elif ord(s1[i]) == ord(s2[i]):
                continue
            else:
                return b

        if len1 < len2:
            return a
        else:
            return b

# n = int(input())
# lst = []
# for s in range(n):
#     lst.append(input())
# print(lst)

# lst = [input().strip() for _ in range(n)]
# print(lst)

# min_str = lst[0]
# for s in lst[1:]:
#     min_str = com_dict(min_str, s)
# print(min_str)

# ret = min(lst, key=lambda x: x.lower())
# print(ret)

# s = input('s: ')
# n = 0
# cur = ''
# ret = ''
# tmp = ''
# for i in s:
#     if cur != i:
#         tmp = i
#         cur = i
#         n = 1
#         ret += tmp
#     else:
#         if n == 1:
#             ret = ret[:len(ret) - 1]
#         else:
#             ret = ret[:len(ret) - 2]
#         n += 1
#         tmp = str(n) + i
#         ret += tmp
#
# print(ret)

# s = input().strip()
# if not s:
#     print('none')
#     exit()
#
# res = []
# count = 1
# cur_char = s[0]
#
# for c in s[1:]:
#     if cur_char == c:
#         count += 1
#     else:
#         if count == 1:
#             res.append(cur_char)
#         else:
#             res.append(str(count) + cur_char)
#
#         count = 1
#         cur_char = c
#
# if count == 1:
#     res.append(cur_char)
# else:
#     res.append(str(count) + cur_char)
#
# print(''.join(res))

# def repeat(n, s):
#     if n > len(s):
#         print('invalid input')
#
#     suffix = s[-n:]
#     print(s, suffix)
#     print(s + suffix * n)
#
# n = int(input())
# print(repeat(n, input()))

# def repeat(n, s):
#     res = s
#     if n > len(s):
#         print('invalid input')
#
#     for i in range(n, 0, -1):
#         res += s[-i:]
#
#     print(res)
#
# n = int(input())
# print(repeat(n, input()))

# s = '@There@is@no@royal@road@to@learning.@'
# print(s.replace('@', ' ').strip())

# import random
# l1 = ['1', '2', '3']
# l2 = ['a', 'b', 'c']
# l3 = ['x', 'y', 'z']
#
# s = random.choice(l1) + random.choice(l2) + random.choice(l3)
# print(s)

# while True:
#     s1, s2 = input('s: ').split()
#     if s1[-1] == s2[0]:
#         print('continue')
#     else:
#         break