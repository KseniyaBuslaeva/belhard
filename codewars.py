# """"There is an array with some numbers. All numbers are equal except for one. Try to find it!"""
# def find_uniq(arr):
#     arr.sort()
#     if arr[0] == arr[1]:
#         return arr[-1]
#     else:
#         return arr[0]
#
#
# print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
# print(find_uniq([ 0, 0, 0.55, 0, 0 ]))


# """Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched."""
# def pig_it(text):
#     reversed_text = ''
#     for word in text.split():
#         if word.isalpha():
#             reversed_text += word[1::] + word[0:1:] + 'ay'
#         else:
#             reversed_text += word
#         reversed_text += ' '
#
#     if reversed_text[-1::] == ' ':
#         return reversed_text[:-1:]
#     else:
#         return reversed_text
#
#
# print(pig_it('Pig latin is cool'))  # igPay atinlay siay oolcay
# print(pig_it('O tempora o mores !'))  # Oay emporatay oay oresmay !


# """The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
# What if the string is empty? Then the result should be empty object literal, {}."""
# def count(string):
#     set_symbols = set(string)
#     dict_symbol = {}
#     if len(string) > 0:
#         for symbol in set_symbols:
#             dict_symbol[symbol] = string.count(symbol)
#         return dict_symbol
#     else:
#         return {}
#
#
#
# count('aba')# {'a': 2, 'b': 1}
# count('')# {}


# """https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python
# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
# Notes:Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered."""
#
# def scramble(s1, s2):
#     set_s1 = sorted(set(s1))
#     set_s2 = sorted(set(s2))
#
#     dict_symbols_s1 = {}
#     dict_symbols_s2 = {}
#     for symbol in set_s2:
#         dict_symbols_s2[symbol] = s2.count(symbol)
#
#     for symbol in set_s1:
#         dict_symbols_s1[symbol] = s1.count(symbol)
#
#     for key in dict_symbols_s2:
#         if dict_symbols_s1.get(key) != None:
#             if dict_symbols_s2[key] <= dict_symbols_s1[key]:
#                 continue
#             else:
#                 return False
#         else:
#             return False
#     return True
#
#
# print(scramble('rkqodlw', 'world')) #==> True
# print(scramble('cedewaraaossoqqyt', 'codewars')) #==> True
# print(scramble('katas', 'steak')) #==> False
# print(scramble('jlrflfijsb', 'bfjfflj')) #==> False


# """https://www.codewars.com/kata/525c65e51bf619685c000059/train/python
# Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.
# Can you help him to find out, how many cakes he could bake considering his recipes?
#
# Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object)
# and returns the maximum number of cakes Pete can bake (integer).
# For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
# Ingredients that are not present in the objects, can be considered as 0."""
#
#
# def cakes(recipe, available):
#     cakes_number = []
#     if set(recipe) <= set(available):
#         for key in recipe:
#             if available.get(key) // recipe.get(key) > 0:
#                 cakes_number.append(available.get(key) // recipe.get(key))
#             else:
#                 return 0
#         return min(cakes_number)
#     else:
#         return 0
#
#
# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# print(cakes(recipe, available))
#
# recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# available = {"sugar": 500, "flour": 2000, "milk": 2000}
# print(cakes(recipe, available))
#
# recipe = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
# available = {'sugar': 500, 'flour': 2000, 'milk': 2000, 'apples': 15, 'oil': 20}
# print(cakes(recipe, available))


"""https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise."""

def snail(snail_map):
    rows_num = len(snail_map)
    firs_row = snail_map[0]
    last_row = snail_map[rows_num-1]
    path = []
    row = 0
    current_row = 0

    path.append(firs_row)

    while row < rows_num:
        path.append(firs_row[-2:2:])
        current_row = row + 1
        while current_row < rows_num-1:
            path.append(snail_map[current_row][-1::])
            current_row += 1

        path.append(last_row[::-1])

        current_row = current_row - 1
        while current_row > row:
            path.append(snail_map[current_row][:1:])
            current_row -= 1
        row += 1
        firs_row = snail_map[row]



    return path


# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]] #[1,2,3,6,9,8,7,4,5]
# print(snail(array))
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]] # [1,2,3,4,5,6,7,8,9]
# print(snail(array))

array = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]] #[1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
print(snail(array))
