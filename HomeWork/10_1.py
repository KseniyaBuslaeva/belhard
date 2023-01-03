"""1. Дан многострочный файл txt"""
with open('10_1.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

N = int(input('input N: '))

"""а) разбить файл на N(вводится с клавиатуры) файлов построчно"""
# n = 0
# if len(lines) > N > 0:
#     while n < N:
#         with open('10_1_a_{}.txt'.format(n), 'w', encoding='utf-8') as file:
#             file.writelines(lines[n])
#         n += 1
# else:
#     print('N should be less than {} and more than 0'.format(len(lines)))

"""б) разбить файл на несколько файлов по N строк"""
import math
num = 0
files_num = math.ceil(len(lines) / N)

for files in range(files_num):
    with open('10_1_b_{}.txt'.format(files), 'w', encoding='utf-8') as file:
        while num < N:
            try:
                file.writelines(lines[files*N+num])
                num += 1
            except:
                break
        num = 0
        files += 1
