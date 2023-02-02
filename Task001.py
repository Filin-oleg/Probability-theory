# Задание:Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.


from math import factorial


def combinations(n, k):
    return (factorial(n)/(factorial(k)*factorial(n-k)))


P = combinations(13, 4)/combinations(52, 4)
print(f'Вероятность того, что все карты - крести = {round(P*100,2)}%')


P2 = 1-combinations(48, 4)/combinations(52, 4)
print(f'Вероятность того, что среди 4-х карт окажется хотя бы один туз = {round(P2*100,2)}%')
