fo = open('aaa.txt', 'w')
fo.write('aaa\nbbb\nccc\nddd')
print('name ', fo.name)
print('close ', fo.closed)
print('mode ', fo.mode)
fo.readline()
fo.close()
print('close ', fo.closed)


# with open('dummy.txt', 'r') as reader:
#     print(reader.readline())
#     print(reader.readline())
#     print(reader.readline())
#
# with open('dummy.txt', 'r') as reader:
#     line = reader.readline()
#     while line:
#         print(line, end='')
#         line = reader.readline()
#
# with open('dummy.txt', 'r') as reader:
#     while True:
#         line = reader.readline()
#         # if line == '':
#         #     break
#         if not line:
#             break
#
#         print(line, end='')
#
# with open('dummy.txt', 'r') as reader:
#     print(reader.readlines())
#
# with open('dummy.txt', 'r') as reader:
#     print(next(reader))
#     print(next(reader))
#
# with open('dummy.txt', 'r') as reader:
#     print(reader.readline())
#     print(reader.tell())
#     print(reader.readline())
#     print(reader.tell())
#
# with open('dummy.txt', 'r') as reader:
#     print(reader.readline())
#     reader.seek(0)
#     print(reader.readline())
#     reader.seek(10)
#     print(reader.readline())
#
# with open('test.txt', 'w+') as reader:
#     with open('dummy.txt', 'r') as f:
#         content = f.read()
#         reader.write(content)
#
#     reader.seek(0)
#     print(reader.read())
#
#     reader.seek(0)
#     reader.truncate(20)
#     print(reader.read())
#
# a, b = map(int, input('input: ').strip().split())
# print(f'{a} {b}')
#
# lst = list(map(int, input('input: ').strip().split()))
# print(lst)
#
# lst = input('input: ').strip().split()
# print(lst)
#
# lst = list(input('input: '))
# print(lst)

import os
# files = []
# print(os.getcwd())
# for file in os.listdir(os.getcwd()):
#     print(file)
#     if os.path.isfile(file) and file.endswith('.txt'):
#         files.append(file)
# print(files)
#
# files = [file for file in os.listdir(os.getcwd()) if os.path.isfile(file) and file.endswith('.txt')]
# print(files)
#
# 文件路径操作
# import os
# path = os.getcwd()
# print(path)
# dir_path = os.path.dirname(path)
# print(dir_path)
#
# tmp_path = path + '/tmp'
# if not os.path.exists(tmp_path):
#     os.mkdir(tmp_path)
# lst = os.listdir(path)
# print(lst)
#
# os.chdir(tmp_path)
# print(os.getcwd())
# os.chdir(tmp_path + '/..')
# print(os.getcwd())
# os.rmdir(tmp_path)
# print(os.listdir(path))

# # DFS
# import os
# path = os.getcwd()
# dir_path = os.path.dirname(path)
#
# def list_dir_dfs(cur_path):
#     print(cur_path)
#     for item in os.listdir(cur_path):
#         tmp = os.path.join(cur_path, item)
#         if os.path.isfile(tmp):
#             print(item)
#         elif os.path.isdir(tmp):
#             list_dir_dfs(tmp)
#
# list_dir_dfs(dir_path)

## BFS
# import os
# path = os.getcwd()
# dir_path = os.path.dirname(path)
#
# def list_dir_bfs(cur_path):
#     lst = [cur_path]
#     while lst:
#         cur = lst.pop(0)
#         print(cur)
#         print(os.listdir(cur))
#
#         for item in os.listdir(cur):
#             tmp = os.path.join(cur, item)
#
#             if os.path.isfile(tmp):
#                 print(item)
#             elif os.path.isdir(tmp):
#                 lst.append(tmp)
#
# list_dir_bfs(dir_path)

# # 处理二进制文件
# import pickle
#
# # 定义各种类型的数据
# i = 13000000  # 整数
# a = 99.056  # 浮点数
# s = '中国人民123abc'  # 字符串
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 嵌套列表
# tu = (-5, 10, 8)  # 元组
# coll = {4, 5, 6}  # 集合
# dic = {'a': 'apple', 'b': 'banana', 'g': 'grape', 'o': 'orange'}  # 字典
#
# # 将所有数据整合到一个列表中
# data = [i, a, s, lst, tu, coll, dic]
#
# # 使用 with 语句安全地打开文件
# with open('sample_pickle.dat', 'wb') as f:
#     try:
#         # 首先写入数据项的数量
#         pickle.dump(len(data), f)
#
#         # 遍历并写入每个数据项
#         for item in data:
#             pickle.dump(item, f)
#
#         print("数据成功写入文件！")
#
#     except Exception as e:
#         # 捕获并处理可能的异常
#         print(f'写文件异常: {str(e)}')
#
# with open('sample_pickle.dat', 'rb') as f:
#     n = pickle.load(f)
#     for i in range(n):
#         x = pickle.load(f)
#         print(x)

# 字典处理火星文
# mars_dic = {}
#
# with open('code.txt', 'r', encoding='utf-8') as f:
#     while True:
#         pair = f.readline()
#         if not pair:
#             break
#
#         key, value = pair.strip().split()
#         mars_dic[key] = value
#
#     # print(mars_dic)
#
# while True:
#     txt = input('input text: ')
#
#     if txt == 'exit':
#         break
#
#     ret = ''
#     for i in txt:
#         tmp = mars_dic.get(i)
#         if not tmp:
#             ret = 'invalid text!'
#             break
#
#         ret += tmp
#
#     print(ret)