"""Get roots of square equation."""


def get_discriminant(a, b, c):
    """Get discriminant square equation a*x^2 + b*x + c = 0.
    D = b^2 - 4*a*c
    :param a: coefficient before x^2.
    :param b: coefficient before x.
    :param c: coefficient without x.
    :return: discriminant.
    """
    return b ** 2 - 4 * a * c


def get_roots_square_equation(a, b, c):
    """Get roots of square equation a*x^2 + b*x + c = 0.
    x = (-b +-D^0.5)/2*a
    :param a: coefficient before x^2.
    :param b: coefficient before x.
    :param c: coefficient without x.
    :return: roots.
    """
    discriminant = get_discriminant(a, b, c)
    if discriminant < 0:
        return "Not roots."
    if discriminant == 0:
        x1 = (- b + discriminant ** 0.5) / 2 * a
        return [x1]
    else:
        x1 = (- b + discriminant ** 0.5) / 2 * a
        x2 = (- b - discriminant ** 0.5) / 2 * a
        return [x1, x2]


if __name__ == '__main__':
    get_roots_square_equation(1, -2, -3)
