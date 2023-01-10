#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
if __name__ == '__main__':
    sentence = input('Enter a sentence: ')
    print(sentence.replace(' ', '-'))
    print('-'.join(sentence.split(' ')))
    