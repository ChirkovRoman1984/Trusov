import pytest

from lesson_03.models.human import Human
from lesson_03.models.man import Man
from lesson_03.models.woman import Woman


@pytest.fixture
def humans() -> dict[str, Man | Woman]:
    return {
        'dima': Man(first_name='Дима', last_name='Сидоров', age=25, happiness=20, stamina=10, money=0),
        'vasya': Man(first_name='Вася', last_name='Синегубов', age=35),
        'natasha': Woman(first_name='Наташа', last_name='Петрова', age=18, happiness=70, stamina=30, money=500),
        'katya': Woman(first_name='Катя', last_name='Иванова', age=22),
        'human': Human(first_name='Иван', last_name='Иванов', age=20),
    }
