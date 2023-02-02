# Задание 3: В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

from math import factorial


def combinations(n, k):
    return (factorial(n)/(factorial(k)*factorial(n-k)))


P = combinations(9, 3)/combinations(15, 3)
print(
    f'Вероятность того, что все извлеченные детали окрашены = {round(P*100,2)}%')
