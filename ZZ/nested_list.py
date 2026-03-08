# lst = [[1, 2, 3], [4, 5, 5]]
# print(lst)

# lst = []
# for i in range(2):
#     row = []
#     for j in range(3):
#         row.append(i * 3 + j + 1)
#     lst.append(row)
# print(lst)

# [表达式 for 变量 in 可迭代对象 if 条件]
# lst = [[i * 3 + j + 1 for j in range(3)] for i in range(2)]
# print(lst)
#
# mapping = [a + b + c for a in '01' for b in '01' for c in '01']
# print(mapping)
#
# odd = [i for i in range(10)]
# print(odd)
#
# odd = []
# for i in range(10):
#     if i % 2 == 1:
#         odd.append(i)
# print(odd)

# [表达式 for 变量 in 可迭代对象 if 条件]
# even = [i * 2 for i in range(5) if i % 2 ==0]
# print(even)




# lst = [[i * 3 + j + 1 for j in range(3)] for i in range(2)]
# lst[1][2] = 99
# print(lst)
# print(lst[0])
# lst = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]
# print(lst)

# lst = []
# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(0)
#     lst.append(row)
# print(lst)

# 列表推到表达式
# lst = [[0 for j in range(5)] for i in range(5)]
# print(lst)

# lst = []
# for i in range(5):
#     lst.append([0] * 5)
# print(lst)

# lst = [[0] * 5 for i in range(5)]
# print(lst)
# for i in lst:
#     print(id(i))

# 分配了5个空间，每个空间里面都是0
# lst = [0] * 5
# print(lst)

# 引用问题
# lst = [[0] * 5] * 5
# print(lst)
# lst[0][4] = 99
# print(lst)
# for i in lst:
#     print(id(i))

# lst = []
# inner = [0] * 5
# for i in range(5):
#     lst.append(inner)
# # lst[0][4] = 99
# inner[4] = 99
# print(lst)

# 遍历二维列表
# lst = [[i * 3 + j + 1 for j in range(3)] for i in range(2)]
# print(lst)

# for row in lst:
#     for element in row:
#         print(element)
#
# print('----')
#
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         print(lst[i][j])
#
# print('----')
#
#
# 逆序遍历
# for i in range(len(lst) - 1, -1, -1):
#     for j in range(len(lst[i]) - 1, -1, -1):
#         print(lst[i][j])
# #
# # print('----')
# #
# for row in lst[::-1]:
#     for element in row[::-1]:
#         print(element)
# #
# # print('----')
# #
# for i in range(len(lst))[::-1]:
#     for j in range(len(lst[i]))[::-1]:
#         print(lst[i][j])



# # 生成一个5*5的列表，从1~25
lst = [[i * 5 + j + 1 for j in range(5)] for i in range(5)]
# lst = [[1, 2, 3, 4, 5],
#        [6, 7, 8, 9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]]
# print(lst)

# for i in range(5):
#     for j in range(i, 5):
#         print(lst[i][j])
#
# for i in range(5):
#     for j in range(i + 1):
#         print(lst[i][j])
#
#
# for i in range(len(lst)):
#     for j in range(i, len(lst[i])):
#         print(lst[i][j], end=' ')
#     print()
#
# for i in range(len(lst)):
#     for j in range(0, i + 1):
#         print(lst[i][j], end=' ')
#     print()
#
#

def rotate_matrix(n):
    matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
    print(matrix)

    # 方法一：位置映射，通过临时二维列表来实现
    ret = [[0] * n for x in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n - i - 1] = matrix[i][j]

    for x in ret:
        print(x)

    # 方法二：环形旋转，for外层循环是有矩阵有几层需要旋转，for内层循环是每一层矩阵需要旋转几次
    # for i in range(len(matrix) // 2):
    #     m = len(matrix[i])
    #     for j in range(i, m - 1 - i): # 第一行遍历n-1个，最后一个不用遍历
    #         tmp = matrix[i][j]
    #         matrix[i][j] = matrix[m - j - 1][i]
    #         matrix[m - j - 1][i] = matrix[m - i - 1][m - j - 1]
    #         matrix[m - i - 1][m - j - 1] = matrix[j][m - i - 1]
    #         matrix[j][m - i - 1] = tmp
    #
    # for x in matrix:
    #     print(x)

    # 方法三：先倒序，再转置
    # m = len(matrix)
    #
    # # 1. 切片倒置
    # # matrix = matrix[::-1]
    #
    # # 2.原地倒置，等同于切片倒置
    # for i in range(m // 2):
    #     matrix[i], matrix[m - 1 - i] = matrix[m - 1 - i], matrix[i]
    #
    # for i in matrix:
    #     print(i)
    #
    # # 外层循环是每一行都需要遍历，内层循环是每一行未置换的元素要遍历
    # for i in range(n):
    #     for j in range(i, n):
    #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    #
    # for x in matrix:
    #     print(x)

rotate_matrix(3)


#
# # 按列遍历二维列表
# def list_list():
#     lst = [[i * 3 + j + 1 for j in range(3)] for i in range(2)]
#     print(lst)
#
#     # for j in range(len(lst[0])):
#     #     for i in range(len(lst)):
#     #         print(lst[i][j])
#
#     for i in range(len(lst)):
#         for j in range(len(lst[i])):
#             print(lst[i][j])
#
#     print()
#
#     # 逆序
#     for i in range(len(lst) - 1, -1, -1):
#         for j in range(len(lst[0]) - 1, -1, -1):
#             print(lst[i][j])
#
#
# list_list()



# Homework

# def abc(a):
#
#     n = len(a)
#     m = []
#
#     for i in range(n):
#         for j in range(i, n):
#             m.append(str(a[i][j]))
#     print(' '.join(m))
#
# a = []
# num = 1
# for i in range(5):
#     c = []
#     for j in range(5):
#         c.append(num)
#         num = num + 1
#     a.append(c)
# abc(a)

# lst = [[1, 2, 3, 4, 5],
#       [6, 7, 8, 9, 10],
#       [11, 12, 13, 14, 15],
#       [16, 17, 18, 19, 20],
#       [21, 22, 23, 24, 25]]
#
# abc = []
# for i in range(5):
#     for j in range(i + 1):
#         abc.append(str(lst[i][j]))
#
# print(' '.join(abc))


