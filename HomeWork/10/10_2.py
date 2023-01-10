"""В файле записано стихотворение. Выведите его на экран, а также
укажите, каких слов в нем больше: начинающихся на гласную или на
согласную букву (без учета регистра)?"""

with open('10_2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

string_poem = ""
count_vowel_words = 0
count_consonants_words = 0
vowels = "aeuioy"

for line in lines:
    if not line.isspace():
        print(line)
        string_poem += line.lower()
    else:
        continue

words_poem = string_poem.split()
n = 0

while n < len(words_poem):
    if words_poem[n][:1:] in vowels:
        count_vowel_words += 1
    else:
        count_consonants_words += 1
    n += 1

print('vowel words: ', count_vowel_words)
print('consonants words: ', count_consonants_words)
