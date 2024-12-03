import pytest

from lesson_03.models.human import Human


class TestHuman:
    def setup_method(self):
        self.human = Human("Иван", "Иванов", 30)

    def test_initialization(self):
        assert self.human.first_name == "Иван"
        assert self.human.last_name == "Иванов"
        assert self.human.age == 30
        assert self.human.happiness == 50
        assert self.human.stamina == 100
        assert self.human.money == 1000

    def test_first_name_setter(self):
        self.human.first_name = "Алексей"
        assert self.human.first_name == "Алексей"

        with pytest.raises(TypeError):
            self.human.first_name = 123  # Неверный тип

        with pytest.raises(ValueError):
            self.human.first_name = "A" * 21  # Слишком длинное имя

    def test_last_name_setter(self):
        self.human.last_name = "Сергеев"
        assert self.human.last_name == "Сергеев"

        with pytest.raises(TypeError):
            self.human.last_name = 123  # Неверный тип

        with pytest.raises(ValueError):
            self.human.last_name = "A" * 21  # Слишком длинная фамилия

    def test_age_setter(self):
        self.human.age = 30
        assert self.human.age == 30

        with pytest.raises(TypeError):
            self.human.age = "30"  # Неверный тип

        with pytest.raises(ValueError):
            self.human.age = -1  # Отрицательный возраст

        with pytest.raises(ValueError):
            self.human.age = 121  # Слишком большой возраст

    def test_happiness_setter(self):
        self.human.happiness = 70
        assert self.human.happiness == 70

        with pytest.raises(TypeError):
            self.human.happiness = "70"  # Неверный тип

        with pytest.raises(ValueError):
            self.human.happiness = -1  # Отрицательное счастье

    def test_stamina_setter(self):
        self.human.stamina = 80
        assert self.human.stamina == 80

        with pytest.raises(TypeError):
            self.human.stamina = "80"  # Неверный тип

        with pytest.raises(ValueError):
            self.human.stamina = -1  # Отрицательная выносливость

    def test_money_setter(self):
        self.human.money = 500
        assert self.human.money == 500

        with pytest.raises(TypeError):
            self.human.money = "500"  # Неверный тип

        with pytest.raises(ValueError):
            self.human.money = -1  # Отрицательные деньги

    def test_eat(self):
        assert self.human.eat() == "Иван Иванов похавал"
        assert self.human.stamina == 110
        assert self.human.money == 900

        self.human.money = 50
        assert self.human.eat() == "Иван Иванов поел и потратил все деньги!"
        assert self.human.money == 0

        assert self.human.eat() == "Иван Иванов не может заплатить за еду"

    def test_work(self):
        assert self.human.work() == "Иван Иванов поработал"
        assert self.human.stamina == 90
        assert self.human.money == 1500

        self.human.stamina = 5
        assert self.human.work() == "Иван Иванов поработал и потратил все силы!"
        assert self.human.stamina == 0  # Тут стамина должна обнулиться
        assert self.human.money == 2000  # Должно быть 1500 + 500 = 2000

        assert self.human.work() == "Иван Иванов не может работать, у него нет сил"

    def test_full_name(self, humans):
        assert self.human.full_name == 'Иван Иванов'
