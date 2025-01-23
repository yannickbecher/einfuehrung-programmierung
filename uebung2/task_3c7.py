import math


def calc_pi(difference: float) -> None:
    pi: float = 0.0
    durchlauefe: int = 0

    while abs(pi - math.pi) > difference:
        pi = pi + (-1)**durchlauefe * 4 / (2 * durchlauefe + 1)
        print(pi)
        durchlauefe += 1

    print(durchlauefe)


calc_pi(0.000001)