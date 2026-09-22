import sys
import random
from time import time


# You will need to implement this function and change the return value.
def mod_exp(x: int, y: int, N: int) -> int:
    if y == 0:
        return 1;
    z = mod_exp(x,y//2,N)
    if y % 2 == 0:
        return (z ** 2) % N
    else:
        return x * (z ** 2) % N

def fermat(N: int, k: int) -> bool:
    a = random.randint(2,N)
    for i in range(k):
        if mod_exp(a, N - 1, N) != 1:
            return False
    return True


def miller_rabin(N: int, k: int) -> bool:
    """
    Returns True if N is prime
    """
    d = N - 1
    s = 0
    a = random.randint(2, N - 1)
#    d = (N-1) / 2 ** k
    for i in range(k):
        if N % 2 == 0:
            return False
        x = mod_exp(a, d, N)
        if x != 1 and x != N-1:
            return False
    return True



def generate_large_prime(n_bits: int) -> int:
    while(True):
        possible = random.getrandbits(n_bits)
        if fermat(possible,5):
            return possible

def main(n_bits: int):
    start = time()
    large_prime = generate_large_prime(n_bits)
    print(large_prime)
    print(f'Generation took {time() - start} seconds')


if __name__ == '__main__':
    main(int(sys.argv[1]))
