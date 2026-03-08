# 通过input输入任意一个字符串，使用for循环，逆序输出每一个字符以及字符对应的index
# s = input('input string: ')
# for i in range(len(s) - 1, -1, -1):
#     print(i, s[i])

# 通过编写for循环计算从1到100（包括100）之间有多少个能被2整除但不能被5整除的数的个数（提示：这里要在for循环之前先声明一个变量total，每次循环的时候，满足判断条件的时候给total+1）
# total = 0
# for i in range(1, 101):
#     if i % 2 == 0 and i % 5 != 0:
#         total += 1
# print(total)

# 通过编写 for 循环计算从 1 到 100（包括100）所有整数的和
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

# 1. 遍历 1 到 50 的所有整数（利用range生成序列），筛选出其中“既是 3 的倍数、又是 5 的倍数”的数，放到一个列表中，打印这个列表
# 2. 打印这些数的个数
# 3. 计算它们的总和，打印结果
# lst = []
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         lst.append(i)
# print(lst)
# print(len(lst))
#
# total = 0
# for j in lst:
#     total += j
# print(total)

# 1. 通过input()获取一个整数n
# 2. 画一颗圣诞树，圣诞树三角形的高度等于n
# n = int(input('input n: '))
# for i in range(n):
#     print(' ' * (n - i - 1) + '*' * (2 * i + 1))
# print(' ' * (n - 1) + '|')

# 1. 利用range函数生成20到10之间（包含20和10）、步长为3的整数序列”，并将序列转为列表lst1，不能使用for循环，要用list()函数直接生成列表，并打印结果
# 2. 使用for循环，把lst1中每个数的平方(**是平方)组成的新列表lst2，并打印结果
# 3. 遍历lst2，找出其中大于 200 的数，存入列表lst3，并打印结果；
# lst1 = list(range(20, 9, -3))
# print(lst1)
#
# lst2 = []
# for i in lst1:
#     lst2.append(i ** 2)
# print(lst2)
#
# lst3 = []
# for j in lst2:
#     if j > 200:
#         lst3.append(j)
# print(lst3)
