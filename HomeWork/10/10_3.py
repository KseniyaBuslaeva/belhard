"""Дан файл с текстом, необходимо в проанализировать файл и сказать
сколько слов и букв в каждой строке"""
with open('10_2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

marks = '''!-;?:'"\,./&;_'''
words = 0
letters = 0

for line in lines:
#убираем пустые строки
    if line.isspace():
        lines.pop(lines.index(line))
    else:
        sentence_words = line.split()

        words = len(sentence_words)

        for word in sentence_words:
#удаляем знаки пунктуации из слов
            for char in marks:
                word = word.replace(char, '')
            letters += len(word)

        print(line)
        print('words: ', words)
        print('letters: ', letters)
        words = 0
        letters = 0
