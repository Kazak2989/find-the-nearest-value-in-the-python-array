# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

list_1 = [1, 2, 3, 5, 4]
k = 6

def find_nearest(list_1, k):
    nearest = None
    difference = float('inf')
    for number in list_1:
        if abs(number - k) < difference:
            difference = abs(number - k)
            nearest = number
    return nearest
print(find_nearest(list_1, k))