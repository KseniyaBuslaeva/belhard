"""Дан файл с текстом, необходимо в проанализировать файл и сказать
сколько слов и букв в каждой строке"""
with open('10_2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

#marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''
words = 0
letters = 0

for line in lines:
    if line.isspace():
        lines.pop(lines.index(line))
    else:
        sentence_words = line.split()
        words = len(sentence_words)

        for word in sentence_words:
            letters += len(word)

        print('words: ', words)
        print('letters: ', letters)
        words = 0
        letters = 0

print(lines)