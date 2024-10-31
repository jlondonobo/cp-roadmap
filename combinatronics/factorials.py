"""Traditional way of storing ints makes factorial fail."""
import argparse


# O(k), where k in # digits of bigint
def multiply(bigint: list[int], scalar: int):
    residual = 0
    result = []
    for val in bigint:
        tmp = scalar * val + residual
        result.append(tmp % 10)
        residual = tmp // 10

    while residual != 0:
        result.append(residual % 10)
        residual //= 10
    return result


def factorial(n: int) -> list[int]:
    result = [1]
    for scalar in range(2, n + 1):
        result = multiply(result, scalar)

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)

    args = parser.parse_args()

    result = factorial(args.n)
    print(f"Result: {''.join(str(v) for v in reversed(result))}")


if __name__ == "__main__":
    main()
