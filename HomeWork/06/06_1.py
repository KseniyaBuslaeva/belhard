#Написать функцию перевода десятичного числа в двоичное и обратно, без
#использования функции int
def from_dec_to_bin(dec_number):
    bin_number = ''
    while dec_number > 1:
        bin = dec_number % 2
        bin_number += str(bin)
        dec_number = dec_number // 2
    bin_number += str(dec_number)
    return bin_number[::-1]


def from_bin_to_dec(bin_number):
    dec_number = 0
    l = len(str(bin_number))
    for n in range(l):
        dec_number += int(bin_number[n]) * 2 ** (l - n - 1)
    return dec_number


if __name__ == '__main__':
    dec_number = int(input('enter dec number: '))
    print(from_dec_to_bin(dec_number))

    bin_number = input('enter bin number: ')
    print(from_bin_to_dec(bin_number))
