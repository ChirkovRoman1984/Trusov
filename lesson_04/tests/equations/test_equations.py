import pytest

from lesson_02.equations import line_equation, square_equation, cube_equation


class TestEquations:
    def test_line_equation(self):
        assert line_equation(1, 0) == 0.0
        assert line_equation(1, -2) == 2.0
        assert line_equation(0, 0) == float('inf')
        assert line_equation(0, 5) is None

        with pytest.raises(TypeError):
            line_equation("a", 5)
        with pytest.raises(TypeError):
            line_equation(5, "b")

    def test_square_equation(self):
        assert square_equation(1, -3, 2) == (2.0, 1.0)
        assert square_equation(1, 2, 1) == (-1.0, None)  # Один корень
        assert square_equation(1, 0, -4) == (2.0, -2.0)  # Два корня
        assert square_equation(1, 0, 1) == (None, None)  # Нет корней

        with pytest.raises(ValueError):
            square_equation(0, 1, 1)
        with pytest.raises(TypeError):
            square_equation(1, "b", 1)

    def test_cube_equation(self):
        assert cube_equation(1, -6, 11, -6) == pytest.approx((3.0, 1.0, 2.0))
        assert cube_equation(1, 0, 0, 0) == (0.0, None, None)
        assert cube_equation(1, 0, 0, -1) == pytest.approx((1.0, -0.5 + 0.866025j, -0.5 - 0.866025j))
        assert cube_equation(1, 0, 0, 1) == pytest.approx((-1.0, 0.5 + 0.866025j, 0.5 - 0.866025j))
        assert cube_equation(10, 10, 10, 10) == pytest.approx((-1.0, 0 + 1j, 0 - 1j))
        assert cube_equation(10, 5, 5, 5) == pytest.approx(
            (-0.738983, 0.1194918 + 0.813834j, 0.1194918 - 0.813834j)
        )

        with pytest.raises(ValueError):
            cube_equation(0, 1, 1, 1)
        with pytest.raises(TypeError):
            cube_equation(1, 1, "c", 1)
