"""
An algorithm that computes ways to rewrite a word ensuring first letter is not a
vowel using the inclusion-exclusion principle


1. All possible character order
2. All character orders starting with a vowel
"""
import argparse
from collections import Counter
from math import factorial


def compute_rewrites_no_starting_vowels(word: str) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    word = word.lower()
    chars = Counter(word)
    n_vowels = sum(chars[v] for v in vowels)
    
    # TODO: Handle edge cases, meanwhile block.
    assert n_vowels != 0
    assert n_vowels != len(word)

    union = factorial(len(word))
    for count in chars.values():
        if count > 1:
            union //= factorial(count)

    vowel_permutations = 0
    for vowel in vowels:
        if chars[vowel] > 0:
            chars[vowel] -= 1
            remaining_permutations = factorial(len(word) - 1)
            for count in chars.values():
                if count > 1:
                    remaining_permutations //= factorial(count)
            vowel_permutations += remaining_permutations
            chars[vowel] += 1

    return union - vowel_permutations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("word")

    args = parser.parse_args()
    result = compute_rewrites_no_starting_vowels(args.word)
    print(f"Possible rewrites: {result}")


if __name__ == "__main__":
    main()
