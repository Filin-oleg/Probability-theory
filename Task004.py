# Задание 4:В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

from math import factorial


def combinations(n, k):
    return (factorial(n)/(factorial(k)*factorial(n-k)))


P = 1/combinations(100, 2)
print(
    f'Вероятность того, что 2 приобретенных билета окажутся выигрышными = {round(P*100,2)}%')
