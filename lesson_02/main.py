from lesson_02.equations import line_equation, square_equation, cube_equation


def main():
    print('Введите коэффиценты кубического уравнения вида ax^3 + bx^2 + cx + d = 0')
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    d = float(input('d = '))

    x_1, x_2, x_3 = None, None, None
    if a == 0:
        if b == 0:
            x_1 = line_equation(c, d)
        else:
            x_1, x_2 = square_equation(b, c, d)
    else:
        x_1, x_2, x_3 = cube_equation(a, b, c, d)

    if x_1 is None:
        print('Решений нет')
    elif x_2 is None:
        if x_1 == float('inf'):
                print('Решением является любое число')
        else:
            print(f'Решением является x = {x_1}')
    elif x_3 is None:
        print(f'Решением являются:\n{x_1 = }\n{x_2 = }')
    else:
        print(f'Решением являются:\n{x_1 = }\n{x_2 = }\n{x_3 = }')


if __name__ == '__main__':
    main()
