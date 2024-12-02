import random

from lesson_03.models.human import Human


class Man(Human):
    def __init__(self, first_name, last_name, age, happiness=50, stamina=100, money=1_000):
        super().__init__(first_name, last_name, age, happiness, stamina, money)
        self.sex = 'male'

    def fishing(self) -> str:
        if self.stamina <= 0:
            message = f'{self.full_name} не может порыбачить, потому что у него нет сил'
            return message
        if self.money <= 0:
            message = f'{self.full_name} не может порыбачить, потому что у него нет денег'
            return message

        self.money -= random.randint(1, 300)
        self.stamina -= 1
        self.happiness += 1
        if self.money < 0:
            self.money = 0
            message = f'{self.full_name} порыбачил и потратил все деньги!'
            return message
        message = f'{self.full_name} успешно порыбачил'
        return message
