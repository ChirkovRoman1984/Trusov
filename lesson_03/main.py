from lesson_03.models.man import Man
from lesson_03.models.woman import Woman


def new_human(a: Man | Woman, b: Man | Woman, sex='male', first_name='Иван'):
    if not isinstance(a, Man | Woman) or not isinstance(b, Man | Woman):
        raise TypeError('Аргументы должны быть Man или Woman')
    if not isinstance(sex, str) or sex not in ('male', 'female'):
        raise TypeError('sex должен быть строкой и содержать male или female')
    if not isinstance(first_name, str) or len(first_name) > 20:
        raise TypeError('first_name должен быть строкой не больше 20 знаков')

    if a.sex == b.sex:
        print('Давай таким не будем заниматься')
        return None
    else:
        last_name = a.last_name if a.sex == 'male' else b.last_name
        if sex == 'male':
            return Man(first_name, last_name, 0)
        else:
            return Woman(first_name, last_name, 0)


def main():
    a = Man('Иван', 'Иванов', 20, money=100)
    print(a)
    b = Woman('Ирина', 'Петрова', 18)
    print(b)

    print(a.work())
    print(a)

    print(b.shoping())
    print(a.fishing())
    print(a)
    print(b)

    c = new_human(a, b, 'male', 'Антон')
    print(c)


if __name__ == '__main__':
    main()
