import pytest

from lesson_03.models.woman import Woman


class TestMan:
    def test_identity(self, humans):
        expected_natasha = {
            '_first_name': 'Наташа',
            '_last_name': 'Петрова',
            'age': 18,
            'happiness': 70,
            'stamina': 30,
            'money': 500,
            'sex': 'female'
        }
        assert humans['natasha'].__dict__ == expected_natasha

    @pytest.mark.parametrize('money, expected', [
        (1000, 'Наташа Петрова сходила на шоппинг'),
        (0, 'Наташа Петрова не может ничего купить, у нее нет денег!'),
        (1, 'Наташа Петрова потратила все деньги на шоппинге!'),
    ])
    def test_fishing(self, money, expected, humans):
        natasha = humans['natasha']
        natasha.money = money
        assert natasha.shoping() == expected
