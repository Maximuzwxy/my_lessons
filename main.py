a = 12345
c = str(a)
b = []

for i in range(len(c)):
    # b[i] = c[len(c) - 1 - i]
    b.append(c[len(c) - 1 - i])

d = ''.join(b)
print(d)

#################

a = 12345
b = list(str(a))

for i in range(int(len(b)/2)):
    c = b[i]
    b[i] = b[len(b) - 1 - i]
    b[len(b) - 1 - i] = c

b = ''.join(b)
print(b)

#####################

a = 12345
a_len = len(str(a))
total = 0

for i in range(a_len):
    tmp = a % 10
    total += tmp * (10 ** (a_len - 1 -i))
    a = a // 10

print(total)

##############

a = 12345
ret = 0

while a:
    tmp = a % 10
    ret = ret * 10 + tmp
    a = a // 10

print(ret)

############################

# 二进制-八进制
src = '1101111'
# 生成mapping list，为什么下面的循环算出来的个数是8个？
mapping = []
for a in '01':
    for b in '01':
        for c in '01':
            mapping.append(a + b +c)
print(mapping)

# 补齐二进制字符串
if len(src) % 3:
    src = '0' * (3- len(src) % 3) + src

print(src)

dest = ''
for i in range(0, len(src), 3):
    dest += str(mapping.index(src[i:i + 3]))
print(dest)

#######################

# 八进制-二进制
src = '157'
mapping = ['{}{}{}'.format(a, b, c) for a in '01' for b in '01' for c in '01']
dest = ''

for i in range(len(src)):
    dest += mapping[int(src[i])]
dest = dest.lstrip('0')
print(dest)

# mapping = ['{}{}{}'.format(a, b, c) for a in '01' for b in '01' for c in '01']
# ans = mapping[0] + mapping[1] + mapping[2]
# print(ans)

# def is_valid_integer(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False
