import random

from lesson_03.models.human import Human


class Woman(Human):
    def __init__(self, first_name, second_name, age):
        super().__init__(first_name, second_name, age)
        self.sex = 'female'

    def shoping(self):
        print(f'{self.full_name} закупилась')
        self.happiness += random.randint(-5, 5)
        self.money -= random.randint(1, 500)
        if self.money < 0:
            self.money = 0
            print(f'{self.full_name} потратила все деньги!')
