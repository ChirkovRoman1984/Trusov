class Human:
    def __init__(self, first_name, second_name, age):
        self._first_name = first_name
        self._second_name = second_name
        self.age = age
        self.happiness = 50
        self.stamina = 100
        self.money = 1_000

    def eat(self):
        self.stamina += 10
        self.money -= 100
        print(f'{self.full_name} похавал')

    def work(self):
        self.stamina -= 20
        self.money += 500
        print(f'{self.full_name} поработал')

    @property
    def second_name(self):
        return self._second_name

    @property
    def full_name(self):
        return f'{self._first_name} {self._second_name}'

    def __str__(self):
        return (
            f'{self._first_name} {self._second_name}, {self.age} лет:\n'
            f'Счастье: {self.happiness}, Здоровье: {self.stamina}, Деньги: {self.money}\n'
        )
