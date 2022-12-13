#Дан список содержащий в себе различные типы данных, отфильтровать таким
#образом, чтобы остались только строки, использование дополнительного списка
#незаконно

if __name__ == '__main__':
    str_list = ['sdf', 34, 423, {23: '35345ert'}, 'werwe', 4545, "erterte", True]

    index = len(str_list) - 1
    while index > 0:
        if not isinstance(str_list[index], str):
            str_list.pop(index)
        index -= 1

    print(str_list)

