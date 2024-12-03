import random

from lesson_03.models.human import Human


class Woman(Human):
    def __init__(self, first_name, last_name, age, happiness=50, stamina=100, money=1_000):
        super().__init__(first_name, last_name, age, happiness, stamina, money)
        self.sex = 'female'

    def shoping(self) -> str:
        if self.money == 0:
            return f'{self.full_name} не может ничего купить, у нее нет денег!'
        random_happiness = random.randint(-5, 5)
        self.happiness = 0 if self.happiness + random_happiness < 0 else self.happiness + random_happiness
        random_money = random.randint(1, 500)
        self.money = 0 if self.money - random_money < 0 else self.money - random_money
        if self.money == 0 and self.happiness == 0:
            return f'{self.full_name} потратила все деньги и абсолютно несчастна!'
        elif self.money == 0:
            return f'{self.full_name} потратила все деньги на шоппинге!'
        elif self.happiness == 0:
            return f'{self.full_name} несчастна после шоппинга'
        return f'{self.full_name} успешно сходила на шоппинг'
