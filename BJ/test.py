# 通过input输入一个整数n
# 使用if/elif/else
# 如果n<0，则打印invalid input
# 如果0<=n<18，则打印children
# 如果18<=n<60，则打印adult
# 如果n>=60，则打印old people

# Exercise 1
# Enter an integer n using input().
# Use if/elif/else to judge:
# If n < 0: print 'invalid input'
# If 0 <= n < 18: print 'children'
# If 18 <= n < 60: print 'adult'
# If n >= 60: print 'old people'

# n = int(input('n: '))
# if n < 0:
#     print('invalid input')
# elif n < 18:
#     print('children')
# elif n < 60:
#     print('adult')
# else:
#     print('old people')

##################################

# 使用for循环计算1~100的和
# Exercise 2
# Use a for loop to accumulate the sum of numbers from 1 to 100.

# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

##################################

# 使用while循环计算1~100的和
# Exercise 3
# Use a while loop to accumulate the sum of numbers from 1 to 100.

# total = 0
# i = 1
# while i <= 100:
#     total += i
#     i += 1
# print(total)
#
# total = 0
# i = 1
# while True:
#     if i <= 100:
#         total += i
#         i += 1
#     else:
#         break
# print(total)

##################################

# 1. Use a for loop with step to output all numbers divisible by 10 from 100 down to 50.


# for i in range(0, 10, 2):
#     print(i)

# for i in range(1, 101):
#     if i % 5 == 0:
#         print(i)
#

# n = int(input('n: '))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)


# Generate lst with 7 random integers (1-10) using list comprehension, then print lst.
# Extract unique numbers from lst and add them to the visited list (each number only once).






