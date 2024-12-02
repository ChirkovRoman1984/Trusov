from lesson_03.models.man import Man
from lesson_03.models.woman import Woman


def new_human(a: Man | Woman, b: Man | Woman, sex='male', first_name='Иван'):
    if type(a) == type(b):
        print('Давай таким не будем заниматься')
        return None
    else:
        last_name = a.last_name if a.sex == 'male' else b.last_name
        if sex == 'male':
            return Man(first_name, last_name, 0)
        else:
            return Woman(first_name, last_name, 0)


def main():
    a = Man('Иван', 'Иванов', 20, money=0)
    print(a)
    b = Woman('Ирина', 'Петрова', 18)
    print(b)

    a.work()
    print(a)

    print(b.shoping())
    print(a.fishing())
    print(a)
    print(b)

    c = new_human(a, b, 'male', 'Антон')
    print(c)


if __name__ == '__main__':
    main()
