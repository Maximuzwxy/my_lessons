# strip
# s = ' Hello, World! '
# print(len(s))
# # print(s.split())
# s1 = s.strip()
# print(s1)
# print(len(s1))
#
# s2 = s.lstrip()
# print(s2)
# print(len(s2))
#
# s3 = s.rstrip()
# print(s3)
# print(len(s3))

# s = 'hello,world'
# print(s.split(','))
#
# s = 'hello world'
# print(s.split())

# s = 'Python is awesome'
# s1 = 'om'
#
# print(s.find(s1))
# print(s.find(s1, 2, 5))
# print(s.find(s1, 10))
#
# print(s.find('o'))
# print(s.rfind('o'))

# lst = ['apple', 'banana', 'pear']
# s = ','.join(lst)
# print(s)
#
# print(' and '.join(lst))
#
# b = 'Harry has a ballon'
# print(','.join(b))
#
# s = 'abcde'
# print(' '.join(s[::-1]))
# print(' '.join(reversed(s)))
#
# print(b.replace('has', 'had'))
# print(b.replace('a', 'A'))

# s = 'harry Hz Nx'
# print(s.upper())
# print(s.lower())
# print(s.capitalize())

# num = '5'
# letter = 'abcde'
#
# print(num.isnumeric())
# print(num.isalnum())
# print(num.isalpha())
# print(letter.isalpha())

# movie = "2001: A SAMMY ODYSSEY"
# book = "A Thousand Splendid Sharks"
# poem = "sammy lived in a pretty how town"
#
# print(movie.islower())
# print(movie.isupper())
#
# print(book.istitle())
# print(book.isupper())
#
# print(poem.istitle())
# print(poem.islower())

# def last_word(s):
#     lst = s.split()
#     if len(lst) == 0:
#         return ''
#     else:
#         return lst[-1]
#
# ss = input('str: ')
# print(len(last_word(ss)))

# def change(s):
#     if s.isupper():
#         return s.lower()
#     else:
#         return s.upper()
#
# ss = input('s: ')
# print(change(ss))

def compare_str(s1, s2):
    ret = 0
    if len(s1) != len(s2):
        ret = 1
    else:
        if s1 == s2:
            ret = 2
        else:
            if s1.upper() == s2.upper():
                ret = 3
            else:
                ret = 4

    return ret

# while True:
#     s1 = input('s1: ')
#     s2 = input('s2: ')
#     print(compare_str(s1, s2))


# while True:
#     lst = [0] * 26
#
#     s = input('s: ')
#     for i in s:
#         index = ord(i) - ord('a')
#         lst[index] += 1
#     l = lst[::-1]
#     max_c = chr(ord('a') + 25 - l.index(max(l)))
#     print(max(l), max_c)



# palindrome
# s = input('s: ')

# if s == s[::-1]:
#     print(True)
# else:
#     print(False)

# ret = True
# for i in range(len(s) // 2):
#     if s[i] != s[len(s) - i - 1]:
#         ret = False
#         break
# print(ret)

# ret = True
# left, right = 0, len(s) - 1
# while left < right:
#     if s[left] != s[right]:
#         ret = False
#         break
#     left += 1
#     right -= 1
# print(ret)

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

# while True:
#     s = input('s: ')
#     if is_palindrome(s):
#         print(True)
#     else:
#         ret = False
#         for i in range(len(s)):
#             lst = list(s)
#             lst.pop(i)
#             s1 = ''.join(list(lst))
#             if is_palindrome(s1):
#                 ret = True
#                 break
#         print(ret)

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



# s = ['a', 'b']
# a = s.split()
# print(a)

# s = 'abcedf'
# print(' '.join(s))
# print(''.join(reversed(s)))
