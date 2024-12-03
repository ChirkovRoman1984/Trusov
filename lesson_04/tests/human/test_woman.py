import pytest
from unittest.mock import patch

class TestWoman:
    def test_initialization(self, humans):
        woman = humans['natasha']
        assert woman.first_name == "Наташа"
        assert woman.last_name == "Петрова"
        assert woman.age == 18
        assert woman.happiness == 70
        assert woman.stamina == 30
        assert woman.money == 500
        assert woman.sex == 'female'

    @patch('random.randint')  # Мокирование функции randint в модуле random
    def test_shoping(self, mock_randint, humans):
        mock_randint.side_effect = [5, 5]  # Подменяем возвращаемое значение на 5 для happiness и 5 для money
        woman = humans['natasha']
        assert woman.shoping() == 'Наташа Петрова успешно сходила на шоппинг'
        assert woman.money == 495
        assert woman.happiness == 75

        woman.money = 1
        mock_randint.side_effect = [5, 5]
        assert woman.shoping() == 'Наташа Петрова потратила все деньги на шоппинге!'
        assert woman.money == 0
        assert woman.happiness == 80

        mock_randint.side_effect = [5, 5]
        assert woman.shoping() == 'Наташа Петрова не может ничего купить, у нее нет денег!'
        assert woman.money == 0
        assert woman.happiness == 80

        mock_randint.side_effect = [-5, 5]
        woman.money = 100
        woman.happiness = 1
        assert woman.shoping() == 'Наташа Петрова несчастна после шоппинга'
        assert woman.money == 95
        assert woman.happiness == 0

        mock_randint.side_effect = [-5, 5]
        woman.money = 1
        assert woman.shoping() == 'Наташа Петрова потратила все деньги и абсолютно несчастна!'
        assert woman.money == 0
        assert woman.happiness == 0
