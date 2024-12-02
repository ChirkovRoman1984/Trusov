import pytest


class TestMan:
    def test_identity(self, humans):
        expected_dima = {
            '_first_name': 'Дима',
            '_last_name': 'Сидоров',
            'age': 25,
            'happiness': 20,
            'stamina': 10,
            'money': 0,
            'sex': 'male'
        }
        expected_vasya = {
            '_first_name': 'Вася',
            '_last_name': 'Синегубов',
            'age': 35,
            'happiness': 50,
            'stamina': 100,
            'money': 1000,
            'sex': 'male'
        }
        assert humans['dima'].__dict__ == expected_dima
        assert humans['vasya'].__dict__ == expected_vasya

    @pytest.mark.parametrize('money, stamina, expected', [
        (1000, 100,  'Дима Сидоров успешно порыбачил'),
        (0, 100,  'Дима Сидоров не может порыбачить, потому что у него нет денег'),
        (0, 0,  'Дима Сидоров не может порыбачить, потому что у него нет сил'),
        (1000, 0,  'Дима Сидоров не может порыбачить, потому что у него нет сил'),
    ])
    def test_fishing(self, money, stamina, expected, humans):
        dima = humans['dima']
        dima.money = money
        dima.stamina = stamina
        assert dima.fishing() == expected
