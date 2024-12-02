import pytest

from lesson_02.equations import line_equation, square_equation, cube_equation


class TestEquations:
    @pytest.mark.parametrize('a, b, expected', [
        (0, 0, float('inf')),
        (0, 1, None),
        (1, -1, 1),
        (100, -1, 0.01)
    ])
    def test_linear_equation(self, a, b, expected):
        assert line_equation(a, b) == expected

    @pytest.mark.parametrize('a, b, c, expected', [
        (8, 0, 5, (None, None)),
        (-4, 28, -49, (3.5, None)),
        (1, 0, 0, (0, None)),
        (6, 0, -54, (3.0, -3.0)),
        (1, -1, 0, (1.0, 0)),
    ])
    def test_lsquare_equation(self, a, b, c, expected):
        assert square_equation(a, b, c) == expected

    @pytest.mark.parametrize('a, b, c, d, expected', [
        (8, -36, 54, -27, (1.5, None, None)),
        (8, 12, 6, 1, (-0.5, None, None)),
        (5, -8, -8, 5, (2.1306623862918075, -0.9999999999999999, 0.4693376137081928)),
    ])
    def test_cube_equation(self, a, b, c, d, expected):
        assert cube_equation(a, b, c, d) == expected
