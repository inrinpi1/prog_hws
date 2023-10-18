from combinatorics import *
from areas import *


choice = input('Введите "комбинаторика" или "геометрия": ')

if choice == 'комбинаторика':
    combinatorics_func = input('Введите "факториал", "перестановки", "сочетания" или "размещения": ')

    if combinatorics_func == 'факториал':
        num = int(input('Введите число для вычисления факториала: '))
        print(factorial(num))
    elif combinatorics_func == 'перестановки':
        n = int(input('Введите n: '))
        print(permutation(n))
    elif combinatorics_func == 'сочетания':
        n = int(input('Введите n: '))
        m = int(input('Введите m: '))
        print(combination(n, m))
    elif combinatorics_func == 'размещения':
        n = int(input('Введите n: '))
        m = int(input('Введите m: '))
        print(arrangement(n, m))

elif choice == 'геометрия':
    shape = input('Введите "прямоугольник", "квадрат", "треугольник" или "шар": ')
    
    if shape == 'прямоугольник':
        length = float(input('Введите длину: '))
        width = float(input('Введите ширину: '))
        print(rectangle_area(length, width))
    elif shape == 'квадрат':
        side = float(input('Введите длину стороны: '))
        print(square_area(side))
    elif shape == 'треугольник':
        base = float(input('Введите основание: '))
        height = float(input('Введите высоту: '))
        print(triangle_area(base, height))
    elif shape == 'шар':
        radius = float(input('Введите радиус: '))
        print(sphere_area(radius))
