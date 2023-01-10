#Дан словарь, ключ - Название страны, значение - список городов, на вход
#поступает город, необходимо сказать из какой он страны

def get_key(city_name, vocablurary):
    for country in vocabulary.keys():
        for city in vocabulary.get(country):
            if city == city_name:
                return country

if __name__ == '__main__':
    vocabulary = {'belarus': {'mogilev', 'minsk', 'vitebsk'}, 'ukraine': {'odessa', 'kiev', 'lviv', 'donetsk'}}

    city_name = input('enter city name: ')

    print(get_key(city_name, vocabulary))