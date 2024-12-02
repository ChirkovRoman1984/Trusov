import random

from lesson_03.models.human import Human


class Woman(Human):
    def __init__(self, first_name, last_name, age, happiness=50, stamina=100, money=1_000):
        super().__init__(first_name, last_name, age, happiness, stamina, money)
        self.sex = 'female'

    def shoping(self) -> str:
        if self.money <= 0:
            message = f'{self.full_name} не может ничего купить, у нее нет денег!'
            return message
        self.happiness += random.randint(-5, 5)
        if self.happiness < 0:
            self.happiness = 0
        self.money -= random.randint(1, 500)
        if self.money < 0:
            self.money = 0
            message = f'{self.full_name} потратила все деньги на шоппинге!'
            return message
        return f'{self.full_name} сходила на шоппинг'
