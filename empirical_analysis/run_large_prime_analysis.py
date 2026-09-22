import itertools
import json
import os
import sys

this_folder = os.path.dirname(__file__)
sys.path.append(os.path.join(this_folder, ".."))

from prime_number_generation import generate_large_prime

from byu_pytest_utils import (
    measure_runtime,
    compute_average_runtimes,
    print_markdown_table,
)


def _large_primes(size):
    generate_large_prime(size)


def main(input, recursion_limit, error_message):
    measure_runtime(
        _large_primes,
        input,
        recursion_limit=recursion_limit,
        error_message=error_message,
    )

    with open("_large_primes_runtimes.json", "r") as f:
        runtimes = json.load(f)

    ave_runtimes = compute_average_runtimes(runtimes)

    print_markdown_table(ave_runtimes)


if __name__ == "__main__":
    sizes = [64, 128, 256, 512, 1024, 2048]

    recursion_limit = sizes[-1] * 2

    error_message = 'An error has occurred. For more information, see "Using the Empirical Analysis Scripts" on Canvas'

    iterations = 10
    input_tuples_iterator = itertools.chain.from_iterable(
        itertools.product(sizes) for _ in range(iterations)
    )
    input_tuples = sorted(list(input_tuples_iterator))

    main(input_tuples, recursion_limit, error_message)
