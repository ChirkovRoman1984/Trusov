import pytest

from lesson_03.main import new_human
from lesson_03.models.man import Man
from lesson_03.models.woman import Woman


def test_new_human(humans):
    with pytest.raises(TypeError):
        new_human('str', 123)
        new_human('str', humans['vasya'])
        new_human(humans['vasya'], 'str')
        new_human(humans['human'], humans['vasya'])
        new_human(humans['natasha'], humans['vasya'], sex='ale')
        new_human(humans['natasha'], humans['vasya'], sex=123)
        new_human(humans['natasha'], humans['vasya'], first_name=123)
        new_human(humans['natasha'], humans['vasya'], first_name='a'*21)
        new_human(123)
    assert new_human(humans['dima'], humans['vasya'], sex='male', first_name='Иван') is None
    assert new_human(humans['natasha'], humans['katya'], sex='male', first_name='Иван') is None
    assert new_human(humans['dima'], humans['katya'], sex='male', first_name='Иван').__dict__ == Man(
        first_name='Иван',
        last_name=humans['dima'].last_name,
        age=0,
    ).__dict__
    assert new_human(humans['dima'], humans['katya']).__dict__ == Man(
        first_name='Иван',
        last_name=humans['dima'].last_name,
        age=0,
    ).__dict__
    assert new_human(humans['natasha'], humans['vasya'], sex='female', first_name='Лена').__dict__ == Woman(
        first_name='Лена',
        last_name=humans['vasya'].last_name,
        age=0,
    ).__dict__
