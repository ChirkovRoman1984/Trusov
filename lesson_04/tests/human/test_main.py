from lesson_03.main import new_human
from lesson_03.models.man import Man
from lesson_03.models.woman import Woman


def test_new_human(humans):
    assert new_human(humans['dima'], humans['vasya'], sex='male', first_name='Иван') is None
    assert new_human(humans['natasha'], humans['katya'], sex='male', first_name='Иван') is None
    assert new_human(humans['dima'], humans['katya'], sex='male', first_name='Иван').__dict__ == Man(
        first_name='Иван',
        last_name=humans['dima'].last_name,
        age=0,
    ).__dict__
    assert new_human(humans['natasha'], humans['vasya'], sex='female', first_name='Лена').__dict__ == Woman(
        first_name='Лена',
        last_name=humans['vasya'].last_name,
        age=0,
    ).__dict__
