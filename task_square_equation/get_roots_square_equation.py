"""Get roots of square equation."""


def get_discriminant(index_a, index_b, index_c):
    """Get discriminant square equation a*x^2 + b*x + c = 0.
    D = b^2 - 4*a*c
    :param index_a: coefficient before x^2.
    :param index_b: coefficient before x.
    :param index_c: coefficient without x.
    :return: discriminant.
    """
    return index_b ** 2 - 4 * index_a * index_c


def get_roots_square_equation(index_a, index_b, index_c):
    """Get roots of square equation a*x^2 + b*x + c = 0.
    x = (-b +-D^0.5)/2*a
    :param index_a: coefficient before x^2.
    :param index_b: coefficient before x.
    :param index_c: coefficient without x.
    :return: roots.
    """
    discriminant = get_discriminant(index_a, index_b, index_c)
    if discriminant < 0:
        return "Not roots."
    if discriminant == 0:
        root1 = (- index_b + discriminant ** 0.5) / 2 * index_a
        return [root1]
    root1 = (- index_b + discriminant ** 0.5) / 2 * index_a
    root2 = (- index_b - discriminant ** 0.5) / 2 * index_a
    return [root1, root2]


if __name__ == '__main__':
    get_roots_square_equation(1, -2, -3)
