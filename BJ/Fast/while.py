# 通过input输入整数，如果小于0退出循环，如果大于等于0，则输出这个数字的平方
# while True:
#     number = input('input: ')
#     if int(number) < 0:
#         break
#     print(int(number) ** 2)

# 循环随机生成1~100的整数，直到可以被7整除，打印每次生成的数字和总共用的次数
# import random
# total = 0
# while True:
#     a = random.randint(1, 100)
#     print(a)
#     total += 1
#     if a % 7 == 0:
#         break
# print(total)

# 找到能被3和7整除，且个位是5的数字
# a = 0
# while True:
#     a += 1
#     if a % 3 == 0 and a % 7 == 0 and a % 10 == 5:
#         print(a)
#         break

# 打印1~10，但是能被3整除的不打印
# a = 0
# while a < 10:
#     a += 1
#     if a % 3 == 0:
#         continue
#     print(a)


# 猜数字，1~100，看几次可以猜中
# import random
# a = random.randint(1, 100)
# total = 0
# # print(a)
# while True:
#     b = input('input a number: ')
#     c = int(b)
#     total += 1
#
#     if c == a:
#         print('you are right! exit')
#         print('total is ', total)
#         break
#     elif c < a:
#         print('please try a larger one')
#     else:
#         print('please try a smaller one')

# import random
# a = random.randint(1, 100)
# total = 0
# print(a)
# upper = 100
# lower = 1
# while True:
#     b = (upper + lower) // 2
#     total += 1
#
#     if b == a:
#         print('right! exit')
#         print('total is ', total)
#         break
#     elif b < a:
#         print(b, 'try a larger one')
#         lower = b
#     else:
#         print(b, 'try a smaller one')
#         upper = b

# a = 1.5111
# b = round(a, 2)
# print(type(b), b)




