"""Дан файл с текстом, необходимо в проанализировать файл и сказать
сколько слов и букв в каждой строке"""
with open('10_2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    if line.isspace():
        lines.pop(lines.index(line))

print(lines)