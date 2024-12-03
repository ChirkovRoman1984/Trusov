import pytest


class TestMan:
    def test_initialization(self, humans):
        dima = humans['dima']
        assert dima.first_name == "Дима"
        assert dima.last_name == "Сидоров"
        assert dima.age == 25
        assert dima.happiness == 20
        assert dima.stamina == 10
        assert dima.money == 0
        assert dima.sex == 'male'

    def test_fishing(self, humans):
        dima = humans['dima']
        dima.money = 1000
        assert dima.fishing() == 'Дима Сидоров успешно порыбачил'
        assert dima.happiness == 21
        assert dima.stamina == 9

        dima.stamina = 1
        assert dima.fishing() == 'Дима Сидоров порыбачил и потратил на это все силы'
        assert dima.stamina == 0
        assert dima.happiness == 22

        assert dima.fishing() == 'Дима Сидоров не может порыбачить, потому что у него нет сил'
        assert dima.stamina == 0
        assert dima.happiness == 22

        dima.money = 1
        dima.stamina = 1
        assert dima.fishing() == 'Дима Сидоров порыбачил, но потратил все силы и деньги!'
        assert dima.stamina == 0
        assert dima.money == 0
        assert dima.happiness == 23

        dima.stamina = 1
        assert dima.fishing() == 'Дима Сидоров не может порыбачить, потому что у него нет денег'
        assert dima.stamina == 1
        assert dima.money == 0
        assert dima.happiness == 23
