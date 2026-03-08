from collections import deque

de = deque([1, 2, 3, 3, 4, 2, 4])
print(de)

de.append(5)
print(de)

de.appendleft(8)
print(de)

de.pop()
print(de)

de.popleft()
print(de)


