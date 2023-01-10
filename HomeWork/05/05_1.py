#Вывести первые N чисел кратные M и больше K
n = int(input('enter n: '))
m = int(input('enter devisor: '))
k = int(input('enter k: '))
num = k + 1

while n > 0:
    if num % m == 0:
        print(num)
        n -= 1
        num += 1
    else:
        num += 1
