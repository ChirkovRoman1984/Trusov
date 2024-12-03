import math


def validate_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected a number, got {type(value).__name__}")


def line_equation(a, b) -> float | None:
    validate_number(a)
    validate_number(b)

    if a == 0:
        if b == 0:
            return float('inf')
        else:
            return None
    else:
        return float(-b / a)


def square_equation(a, b, c) -> tuple[float | None, float | None]:
    validate_number(a)
    validate_number(b)
    validate_number(c)
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a square equation.")

    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x, None
    else:
        return None, None


def cube_equation(a, b, c, d) -> tuple[float | None, float | None, float | None]:
    validate_number(a)
    validate_number(b)
    validate_number(c)
    validate_number(d)
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a cubic equation.")

    p = (3 * a * c - b**2) / (3 * a**2)
    q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)

    if p == 0 and q == 0:
        return -b / (3 * a), None, None
    else:
        discriminant = q ** 2 / 4 + p ** 3 / 27
        if discriminant == 0:
            x1 = 2 * math.cbrt(-q / 2) - b / (3 * a)
            x2 = -math.cbrt(-q / 2) - b / (3 * a)
            return x1, x2, None
        else:
            if discriminant < 0:
                if q < 0:
                    psi = math.atan(math.sqrt(-discriminant) / (-q / 2))
                elif q > 0:
                    psi = math.atan(math.sqrt(-discriminant) / (-q / 2)) + math.pi
                else:
                    psi = math.pi / 2

                y1 = 2 * math.sqrt(-p / 3) * math.cos(psi / 3)
                y2 = 2 * math.sqrt(-p / 3) * math.cos((psi + 2 * math.pi) / 3)
                y3 = 2 * math.sqrt(-p / 3) * math.cos((psi + 4 * math.pi) / 3)
            else:
                plus_cube_root = math.cbrt(math.sqrt(discriminant) - q / 2)
                minus_cube_root = math.cbrt(-math.sqrt(discriminant) - q / 2)
                y1 = plus_cube_root + minus_cube_root
                y2 = -y1 / 2 + 1j * math.sqrt(3) / 2 * (plus_cube_root - minus_cube_root)
                y3 = -y1 / 2 - 1j * math.sqrt(3) / 2 * (plus_cube_root - minus_cube_root)

            x1 = y1 - b / (3 * a)
            x2 = y2 - b / (3 * a)
            x3 = y3 - b / (3 * a)
            return x1, x2, x3
