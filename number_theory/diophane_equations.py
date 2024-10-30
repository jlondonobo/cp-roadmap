"""A solution exists only if C % GCD(A,B) = 0"""
import argparse


def gcd(a: int, b: int) -> int:
    """Computes greates common denominator."""
    while b != 0:
        a, b = b, a % b
    return a


def has_integral_solution(a: int, b: int, c: int) -> bool:
    """If a, b, and c have integral solution returns True, otherwise returns False."""
    return c % gcd(a, b) == 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("c", type=int)

    args = parser.parse_args()
    
    has_solution = has_integral_solution(args.a, args.b, args.c)
    print(f"Equation {args.a}x + {args.b}y = {args.c}: {has_solution}")


if __name__ == "__main__":
    main()
