class Human:
    def __init__(self, first_name, last_name, age, happiness=50, stamina=100, money=1_000):
        self._first_name = first_name
        self._last_name = last_name
        self.age = age
        self.happiness = happiness
        self.stamina = stamina
        self.money = money

    def eat(self):
        self.stamina += 10
        self.money -= 100
        print(f'{self.full_name} похавал')

    def work(self):
        self.stamina -= 20
        self.money += 500
        print(f'{self.full_name} поработал')

    @property
    def last_name(self):
        return self._last_name

    @property
    def full_name(self):
        return f'{self._first_name} {self._last_name}'

    def __str__(self):
        return (
            f'{self._first_name} {self._last_name}, {self.age} лет:\n'
            f'Счастье: {self.happiness}, Здоровье: {self.stamina}, Деньги: {self.money}\n'
        )
