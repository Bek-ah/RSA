import itertools
import json
import os
import sys

this_folder = os.path.dirname(__file__)
sys.path.append(os.path.join(this_folder, ".."))

from generate_keypair import generate_key_pairs

from byu_pytest_utils import (
    measure_runtime,
    compute_average_runtimes,
    print_markdown_table,
)


def _keypair(size):
    N, e, d = generate_key_pairs(size)
    return size, N, e, d


def _postprocessing(size, N, e, d):
    input = (size, N, e, d)

    with open("_keypairs.json", "r") as f:
        keypairs = list(json.load(f))

    keypairs.append(input)

    with open("_keypairs.json", "w") as f:
        json.dump(keypairs, f, indent=4)


def main(input, recursion_limit):
    with open("_keypairs.json", "w") as f:
        json.dump("", f, indent=4)

    measure_runtime(
        run=_keypair,
        inputs=input,
        recursion_limit=recursion_limit,
        postprocessing=_postprocessing,
    )

    with open("_keypair_runtimes.json", "r") as f:
        runtimes = json.load(f)

    ave_runtimes = compute_average_runtimes(runtimes)

    print_markdown_table(ave_runtimes)


if __name__ == "__main__":
    sizes = [64, 128, 256, 512, 1024, 2048]

    recursion_limit = sizes[-1] * 2

    iterations = 10
    input_tuples_iterator = itertools.chain.from_iterable(
        itertools.product(sizes) for _ in range(iterations)
    )
    input_tuples = sorted(list(input_tuples_iterator))

    main(input_tuples, recursion_limit)
