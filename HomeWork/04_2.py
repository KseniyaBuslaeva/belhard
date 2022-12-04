#без использования collections, написать программу,
# которая будет создавать словарь для подсчитывания количества вхождений каждой буквы в текст введённый с клавиатуры
if __name__ == '__main__':
    sentence = input('Input a text: ')
    abc_list = []
    abc_dict = {}
    print(chr(65))
    for letter in range(65, 90):
        abc_list.append([chr(letter), sentence.count(chr(letter))])

    for letter in range(97, 122):
        abc_list.append([chr(letter), sentence.count(chr(letter))])


    abc_dict = dict(abc_list)
    print(abc_dict)
