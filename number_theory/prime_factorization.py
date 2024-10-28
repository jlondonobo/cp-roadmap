# Requires pre-computing the smallest integer via sieve of eratosthenes
# for every number up to N.

import math as mt


def sieve(n: int) -> list[int]:
    """Computes smallest prime factor using the Sieve function."""
    spf = [1] * n

    for i in range(2, n):
        if spf[i] == 1:
            # For every multiple of i
            for j in range(i, n, i):
                # If you have not found the smalles prime
                if spf[j] == 1:
                    # Then the smalles prime is i
                    spf[j] = i

        # Otherwise, keep at 0.

    return spf


def get_factorization(x: int, spf: list[int]) -> list[int]:
    """Returns prime factorization of x."""
    assert x < len(spf)

    factorization = []
    # If x is not prime
    while x != 1:
        # Divide number by smallest prime factor
        factorization.append(spf[x])
        x = x // spf[x]

        # if spf[x] == 1 we reached a prime number, so we stop
        # otherwise, we keep going with reminder
    return factorization


def main():
    MAXN = 1000
    spf = sieve(MAXN)
    factorization = get_factorization(253, spf)
    print(factorization)


if __name__ == "__main__":
    main()
