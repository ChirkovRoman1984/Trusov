"""
ax**3 + bx**2 + cx + d = 0
формула Кардано
"""
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

p = (3 * a * c - b**2) / (3 * a**2)
q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)

if p == 0 and q == 0:
    x1 = -b / (3 * a)
    print(f'Один корень: {x1 = :.3}')

else:
    D = q ** 2 / 4 + p ** 3 / 27
    if D == 0:
        x1 = 2 * math.cbrt(-q / 2) - b / (3 * a)
        x2 = - math.cbrt(-q / 2) - b / (3 * a)
        print(f'Два корня: {x1 = :.3}, {x2 = :.3}')

    else:
        if D < 0:
            if q < 0:
                t = math.atan(math.sqrt(-D) / (- q / 2))
            elif q > 0:
                t = math.atan(math.sqrt(-D) / (- q / 2)) + math.pi
            else:
                t = math.pi / 2

            y1 = 2 * math.sqrt(-p/3) * math.cos(t / 3)
            y2 = 2 * math.sqrt(-p/3) * math.cos((t + 2 * math.pi) / 3)
            y3 = 2 * math.sqrt(-p/3) * math.cos((t + 4 * math.pi) / 3)

        else:
            y1 = math.cbrt(math.sqrt(D) - q / 2) + math.cbrt(-math.sqrt(D) - q / 2)
            y2 = y1 * (-1 / 2 + 1j * math.sqrt(3) / 2)
            y3 = y1 * (-1 / 2 - 1j * math.sqrt(3) / 2)

        x1 = y1 - b / (3 * a)
        x2 = y2 - b / (3 * a)
        x3 = y3 - b / (3 * a)
        print(f'{x1 = :.3}, {x2 = :.3}, {x3 = :.3}')
