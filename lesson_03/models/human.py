class Human:
    def __init__(self, first_name, last_name, age, happiness=50, stamina=100, money=1_000):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.happiness: int = happiness
        self.stamina: int = stamina
        self.money: int = money

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("First name must be a string.")
        if len(value) > 20:
            raise ValueError("Name cannot exceed 20 characters.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Last name must be a string.")
        if len(value) > 20:
            raise ValueError("Last name cannot exceed 20 characters.")
        self._last_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")
        if value < 0:
            raise ValueError("Age cannot be negative.")
        if value > 120:
            raise ValueError("Age cannot exceed 120.")
        self._age = value

    @property
    def happiness(self):
        return self._happiness

    @happiness.setter
    def happiness(self, value):
        if not isinstance(value, int):
            raise TypeError("Happiness must be an integer.")
        if value < 0:
            raise ValueError("Happiness cannot be negative.")
        self._happiness = value

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        if not isinstance(value, int):
            raise TypeError("Stamina must be an integer.")
        if value < 0:
            raise ValueError("Stamina cannot be negative.")
        self._stamina = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        if not isinstance(value, int):
            raise TypeError("Money must be an integer.")
        if value < 0:
            raise ValueError("Money cannot be negative.")
        self._money = value

    @property
    def full_name(self):
        return f'{self._first_name} {self._last_name}'

    def __str__(self):
        return (
            f'{self._first_name} {self._last_name}, {self.age} лет:\n'
            f'Счастье: {self.happiness}, Здоровье: {self.stamina}, Деньги: {self.money}\n'
        )

    def eat(self):
        self.stamina += 10
        if self.money == 0:
            return f'{self.full_name} не может заплатить за еду'
        self.money = 0 if self.money - 100 < 0 else self.money - 100
        if self.money == 0:
            return f'{self.full_name} поел и потратил все деньги!'
        return f'{self.full_name} похавал'

    def work(self):
        if self.stamina == 0:
            return f'{self.full_name} не может работать, у него нет сил'
        self.stamina = 0 if self.stamina - 10 < 0 else self.stamina - 10
        self.money += 500
        if self.stamina == 0:
            return f'{self.full_name} поработал и потратил все силы!'
        return f'{self.full_name} поработал'
