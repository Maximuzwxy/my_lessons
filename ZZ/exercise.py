# 1. 逆序
# a = input('input:')
# b = []
# for i in range(len(a)):
#     b.append(a[len(a) - 1 - i])
# print(''.join(b))
# #
# c = []
# for i in range(len(a) - 1, -1, -1):
#     c.append(a[i])
# print(''.join(c))
#
# d = list(a)
# for i in range(len(a) // 2):
#     tmp = d[i]
#     d[i] = d[len(a) - 1 - i]
#     d[len(a) - 1 - i] = tmp
# print(''.join(d))
#
# # 以上步骤可以简化

# # 2. 数字化逆序
# a = input('input:')
# b = int(a)
# total = 0
# a_len = len(a)
#
# for i in range(a_len):
#     tmp = b % 10
#     total += tmp * (10 ** (a_len - 1 -i))
#     b = b // 10
#
# print(total)
#
# # 3. 二进制-八进制
# src = input('input:')
# # 生成mapping list，为什么下面的循环算出来的个数是8个？
# mapping = []
# for a in '01':
#     for b in '01':
#         for c in '01':
#             mapping.append(a + b +c)
# print(mapping)
#
# # mapping = []
# # for a in '01':
# #     for b in '01':
# #         for c in '01':
# #             tmp = '{}{}{}'.format(a, b, c)
# #             mapping.append(tmp)
# # print(mapping)
#
# # 补齐二进制字符串
# if len(src) % 3:
#     src = '0' * (3- len(src) % 3) + src
#
# print(src)
#
# dest = ''
# for i in range(0, len(src), 3):
#     dest += str(mapping.index(src[i:i + 3]))
# print(dest)

#######################

# # 4. 八进制-二进制
# src = '157'
# mapping = ['{}{}{}'.format(a, b, c) for a in '01' for b in '01' for c in '01']
# dest = ''
#
# for i in range(len(src)):
#     dest += mapping[int(src[i])]
# dest = dest.lstrip('0')
# print(dest)


# 复习for，包括range的意义
# 输入n，打印0~n中间的所有的偶数，并求和，n的范围是大于等于1小于等于100
# n = int(input('n:'))
# total = 0
# if 1 <= n <= 100:
#     for i in range(0, n + 1, 2):
#         print(i)
#         total += i
# print('total:', total)

# 从1~100，3的倍数，和数字里面带3的，都排除
# n = int(input('n:'))
# total = 0
# if 1 <= n <= 100:
#     for i in range(n + 1):
#         if i % 3 == 0:
#             continue
#         if '3' in str(i):
#             continue
#         print(i)

# a, b = map(int, input('a b: ').split())
# print(a, b)

# lst = input('input some int: ').split()
# print(lst)
# a = '1 2 3 4 5'
# print(a.split())
# b = '123456'
# print(list(b))

# 文件作业
fo1 = open('foo.txt', 'r')
foo1 = open('foo1.txt', 'w')
num = 1
while True:
    a = fo1.readline()
    print(a, end='')
    if not a:
        break
    foo1.write(str(num) + '. ' + a)
    num += 1
fo1.close()
foo1.close()

# for
n = input('input n: ')
for i in range(1, int(n) + 1):
    if i % 3 != 0 and '3' not in str(i):
        print(i)



