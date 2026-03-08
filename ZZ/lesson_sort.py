# n = int(input('n: '))
#
# lst = []
# for i in range(n):
#     inner = []
#     for j in range(n):
#         inner.append(i * n + j + 1)
#     lst.append(inner)
# print(lst)
#
# lst = [[(i * n + j + 1) for j in range(n)] for i in range(5)]
# print(lst)

# lst = []
# for i in range(2):
#     inner = []
#     for j in range(5):
#         inner.append(i * 5 + j + 1)
#     lst.append(inner)
# print(lst)
#
# lst = [[(i * 5 + j + 1) for j in range(5)] for i in range(2)]
# print(lst)

#################
# Selection Sort
# nums = [8, 3, 5, 6, 0, 9, 2, 7, 1, 4]
# print(nums)
# n = len(nums)

# min_index = 0
# for i in range(n):
#     if nums[i] < nums[min_index]:
#         min_index = i
# nums[0], nums[min_index] = nums[min_index], nums[0]
# print(nums)
#
# for i in range(n - 1):
#     min_index = i
#     for j in range(i + 1, n):
#         if nums[j] < nums[min_index]:
#             min_index = j
#     nums[i], nums[min_index] = nums[min_index], nums[i]
# print(nums)

# Buble Sort
# for j in range(n - 1):
#     if nums[j] > nums[j + 1]:
#         nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     print(nums)

# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
# print(nums)

# for i in range(n - 1):
#     flag = False
#     for j in range(n - i - 1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
#             flag = True
#     if not flag:
#         break
# print(nums)

# nums = [79, 4, 48, 68, 2, 64, 56, 42, 21, 1]
# print(nums)
# n = len(nums)

# Insertion Sort
# nums = [1, 3, 8, 9, 2]
# n = len(nums)

# i = n - 2
# target = nums[n - 1]
# while target < nums[i]:
#     nums[i + 1] = nums[i]
#     i -= 1
# nums[i + 1] = target
# print(nums)


# for i in range(1, n):
#     target = nums[i]
#     j = i - 1
#     while j >= 0 and target < nums[j]:
#         nums[j + 1] = nums[j]
#         j -= 1
#     nums[j + 1] = target
# print(nums)

# for i in range(1, n):
#     target = nums[i]
#     flag = False
#     index = 0
#     for j in range(i - 1, -1, -1):
#         if target < nums[j]:
#             nums[j + 1] = nums[j]
#             flag = True
#             index = j
#     if flag:
#         nums[index] = target
#
# print(nums)


################################################
# nums = [8, 3, 5, 6, 0, 9, 2, 7, 1, 4]
# n = len(nums)
#
# for i in range(n - 1):
#     flag = True
#     for j in range(n - 1 - i):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
#             flag = False
#     if flag:
#         break
# print(nums)

# insert sort
# nums = [8, 3, 5, 6, 0, 9, 2, 7, 1, 4]
# n = len(nums)
#
# for i in range(1, n):
#     to_insert = nums[i]
#     j = i - 1
#
#     while j >= 0 and to_insert < nums[j]:
#         nums[j + 1] = nums[j]
#         j -= 1
#     nums[j + 1] = to_insert
#
# print(nums)

