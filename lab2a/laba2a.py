
from functools import reduce
arr = [1, 3, 4, 2, 7]
total = reduce(lambda x, y: x+y,arr)
print(f'Сума всіх елементів масиву - {total}')