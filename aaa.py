# a = 1
# b = 2
# c = a + b
# print(c)

# a = 3
# b = 2

# if a > b:
#     print('a > b')
#     print('asdf')

# for x in 'banana':
#     print(x)
#     print('loop over')

# for i in range(6):
#     print(i)

# a = range(6)
# for i in range(6):
#     print(i)

# for i in range(2, 6):
#     print(i)

# a = 5
# b = 2
# c = a//b
# print(type(c), c)
#
# total = 0
# i = 1
# while i < :
#     i
#     total
# print(total)

# lst = [i for i in range(10)]
# print(lst)
#
# lst = []
# for i in range(10):
#     lst.append(i)
# print(lst)

lst = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(5 * i + j + 1)
    lst.append(row)
print(lst)

import sys


def solve():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        A = int(data[idx])
        B = int(data[idx + 1])
        cA = int(data[idx + 2])
        cB = int(data[idx + 3])
        fA = int(data[idx + 4])
        idx += 5

        if A >= fA:
            print(0)
            continue

        need_A = fA - A

        k_min = (need_A + cA - 1) // cA
        need_B_total = k_min * cB
        need_x = max(0, need_B_total - B)
        print(need_x)


if __name__ == "__main__":
    solve()

