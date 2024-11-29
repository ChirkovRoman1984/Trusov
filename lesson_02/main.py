from lesson_02.equations import line_equation, square_equation, cube_equation


def main():
    print('Введите коэффиценты кубического уравнения вида ax^3 + bx^2 + cx + d = 0')
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    d = float(input('d = '))

    if a == 0:
        if b == 0:
            line_equation(c, d)
        else:
            square_equation(b, c, d)
    else:
        cube_equation(a, b, c, d)


if __name__ == '__main__':
    main()
