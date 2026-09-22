import random
import sys
from time import time
import prime_number_generation

# When trying to find a relatively prime e for (p-1) * (q-1)
# use this list of 25 primes
# If none of these work, throw an exception (and let the instructors know!)
primes = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]

def greatest_common_divisor(a: int, b: int):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)

def extended_euclid(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return 1, 0, a
    [x,y,d] = extended_euclid(b, a % b)
    return y, x - (a // b) * y, d # inverse of a, inverse of b, d = GCD(a,b)

def generate_key_pairs(n_bits) -> tuple[int, int, int]:
    """
    Generate RSA public and private key pairs.
    Randomly creates a p and q (two large n-bit primes)
    Computes N = p*q
    Computes e and d such that e*d = 1 mod (p-1)(q-1)
    Return N, e, and d
    """
    p = prime_number_generation.generate_large_prime(n_bits)
    q = prime_number_generation.generate_large_prime(n_bits)
    N = p * q
    e = 2
    m = (p-1) * (q-1)
    while greatest_common_divisor(e, m) > 1:
        index = random.randint(0, 24)
        e = primes[index]
    d, y, g = extended_euclid(e, m) #d will be in the same order as e in parameter
    if d < 0:
        d = m + d
    return N, e, d




def main(n_bits: int, filename_stem: str):
    start = time()
    N, e, d = generate_key_pairs(n_bits)
    print(f'{time() - start} seconds elapsed')

    public_file = filename_stem + '.public.txt'
    with open(public_file, 'w') as file:
        file.writelines([
            str(N),
            '\n',
            str(e)
        ])
    print(public_file, 'written')

    private_file = filename_stem + '.private.txt'
    with open(private_file, 'w') as file:
        file.writelines([
            str(N),
            '\n',
            str(d)
        ])
    print(private_file, 'written')


if __name__ == '__main__':
    main(int(sys.argv[1]), sys.argv[2])
