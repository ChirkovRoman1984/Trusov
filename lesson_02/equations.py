import math


def line_equation(a, b):
    if a == 0:
        if b == 0:
            print('Бесконечное количество решений')
        else:
            print('Нет решения')
    else:
        x = -b / a
        print(f'{x = }')


def square_equation(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print(f'{x1 = }\n{x2 = }')
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f'{x = }')
    else:
        print('Корней нет')


def cube_equation(a, b, c, d):
    p = (3 * a * c - b**2) / (3 * a**2)
    q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)

    if p == 0 and q == 0:
        x1 = -b / (3 * a)
        print(f'Один корень:\n{x1 = :.2}')
    else:
        discriminant = q ** 2 / 4 + p ** 3 / 27
        if discriminant == 0:
            x1 = 2 * math.cbrt(-q / 2) - b / (3 * a)
            x2 = - math.cbrt(-q / 2) - b / (3 * a)
            print(f'Два корня:\n{x1 = :.2}\n{x2 = :.2}')
        else:
            if discriminant < 0:
                if q < 0:
                    psi = math.atan(math.sqrt(-discriminant) / (- q / 2))
                elif q > 0:
                    psi = math.atan(math.sqrt(-discriminant) / (- q / 2)) + math.pi
                else:
                    psi = math.pi / 2

                y1 = 2 * math.sqrt(-p / 3) * math.cos(psi / 3)
                y2 = 2 * math.sqrt(-p / 3) * math.cos((psi + 2 * math.pi) / 3)
                y3 = 2 * math.sqrt(-p / 3) * math.cos((psi + 4 * math.pi) / 3)
            else:
                y1 = math.cbrt(math.sqrt(discriminant) - q / 2) + math.cbrt(-math.sqrt(discriminant) - q / 2)
                y2 = y1 * (-1 / 2 + 1j * math.sqrt(3) / 2)
                y3 = y1 * (-1 / 2 - 1j * math.sqrt(3) / 2)

            x1 = y1 - b / (3 * a)
            x2 = y2 - b / (3 * a)
            x3 = y3 - b / (3 * a)
            print(f'{x1 = :.2}\n{x2 = :.2}\n{x3 = :.2}')