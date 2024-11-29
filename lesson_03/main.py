from lesson_03.models.man import Man
from lesson_03.models.woman import Woman


def new_human(a: Man | Woman, b: Man | Woman, sex='male', first_name='Иван'):
    if type(a) == type(b):
        print('Давай таким не будем заниматься')
        return None
    else:
        second_name = a.second_name if a.sex == 'male' else b.second_name
        if sex == 'male':
            return Man(first_name, second_name, 0)
        else:
            return Woman(first_name, second_name, 0)


def main():
    a = Man('Иван', 'Иванов', 20)
    print(a)
    b = Woman('Ирина', 'Петрова', 18)
    print(b)

    a.work()
    b.shoping()
    a.fishing()
    print(a)
    print(b)

    c = new_human(a, b, 'male', 'Антон')
    print(c)


if __name__ == '__main__':
    main()
