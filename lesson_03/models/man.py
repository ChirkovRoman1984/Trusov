import random

from lesson_03.models.human import Human


class Man(Human):
    def __init__(self, first_name, second_name, age):
        super().__init__(first_name, second_name, age)
        self.sex = 'male'

    def fishing(self):
        print(f'{self.full_name} порыбачил')
        self.happiness += 1
        self.stamina -= 1
        self.money -= random.randint(1, 300)
        if self.money < 0:
            self.money = 0
            print(f'{self.full_name} потратил все деньги на рыбалке!')
