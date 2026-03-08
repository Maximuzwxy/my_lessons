def empty(stack):
    return len(stack) == 0

def push(stack, data):
    stack.append(data)

def pop(stack):
    if not empty(stack):
        return stack.pop()
    return None

def top(stack):
    if not empty(stack):
        return stack[-1]
    return None

stk = []
print(empty(stk))
push(stk, 1)
push(stk, 2)
push(stk, 3)
print(stk)
pop(stk)
print(top(stk))

def is_matching(s):
    left = 0
    right = 0

    for i in s:
        if i == '(':
            left += 1
        else:
            right += 1

        if left < right:
            return False

    return left == right

# print(is_matching('((()))'))

def stack_matching(s):
    stack = []

    for i in s:
        if i == '(':
            push(stack, i)
        elif stack:
            pop(stack)
        else:
            return False

    return empty(stack)

# print(stack_matching('((()))'))

# def is_matching2(s):
#     left = ['(', '[', '{']
#     right = [')', ']', '}']
#     stack = []
#
#     for i in s:
#         if i in left:
#             push(stack, i)
#         elif i in right:
#             if empty(stack):
#                 return False
#             elif right.index(i) == left.index(top(stack)):
#                 pop(stack)
#             else:
#                 return False
#         else:
#             return False
#
#     return empty(stack)

def is_matching2(s):
    left = ['(', '[', '{']
    right = {')':'(', ']':'[', '}':'{'}
    stack = []

    for i in s:
        if i in left:
            push(stack, i)
        elif empty(stack) or stack.pop() != right[i]:
            return False

    return empty(stack)

# print(is_matching2('()[]{}'))
# print(is_matching2('([{}])'))
# print(is_matching2('([{}])()'))
#
# print(is_matching2('{[]}('))
# print(is_matching2('[()]]'))
# print(is_matching2('[(])'))

s = 'abbaca'
def remove_duplicates(s):
    stack = []
    for i in s:
        if i == top(stack):
            pop(stack)
        else:
            push(stack, i)

    return ''.join(stack)

print(remove_duplicates(s))

def func3():
    print('func3 begins')
    print('func3 ends')

def func2():
    print('func2 begins')
    func3()
    print('func2 ends')

def func1():
    print('func1 begins')
    func2()
    print('func1 ends')

func1()

lst = [4,1,2,3]
print(sorted(lst))

