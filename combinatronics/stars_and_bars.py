"""Using binomial coefficients to find # of ways to distribute identical items."""


def factorial(n: int) -> int:
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact


# Can implement a faster way by simplifying coefficients
def combine(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))


def split_in_groups(stars: int, bars: int) -> int:
    return combine(stars + bars - 1, bars - 1)


def split_in_groups_at_least_one(stars: int, bars: int) -> int:
    return combine(stars - 1, bars - 1)


