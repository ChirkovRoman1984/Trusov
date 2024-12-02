from lesson_03.models.human import Human


class TestHuman:
    def test_identity(self, humans):
        expected = {
            '_first_name': 'Иван',
            '_last_name': 'Иванов',
            'age': 20,
            'happiness': 50,
            'stamina': 100,
            'money': 1000
        }
        assert humans['human'].__dict__ == expected

    def test_full_name(self, humans):
        assert humans['human'].full_name == 'Иван Иванов'

    def test_eat(self, humans):
        human = humans['human']
        human.eat()
        assert human.stamina == 110
        assert human.money == 900

    def test_work(self, humans):
        human = humans['human']
        human.work()
        assert human.stamina == 80
        assert human.money == 1500
