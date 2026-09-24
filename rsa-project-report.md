# Project Report - RSA and Primality Tests

## Baseline

### Design Experience
My discussion partners were Alyse Swenson and Emeline MacJanet.
We discussed how the project overall is organized.
We also went over how to gather empirical data, and additional resources we had found for this project.

### Theoretical Analysis - Prime Number Generation

#### Time
```
def mod_exp(x: int, y: int, N: int) -> int: # O(n^3) since there are n recursions with O(n^2) time
    if y == 0:                              # O(1) - comparison is constant time
        return 1;                           # O(1) - returning is constant time 
    z = mod_exp(x,y//2,N)                   # O(n) - each function call is O(n) time
    if y % 2 == 0:                          # O(1) - comparison is constant time 
        return (z ** 2) % N                 # O(n^2) - returning is constant time 
    else:                                   # O(1) - continuing to the alternate case is constant time 
        return (x * (z ** 2)) % N           # O(n^2) - calculation is constant time (because it uses the mod from earlier steps to keep number length shorter)

def fermat(N: int, k: int) -> bool:     # O(n^3) since the fastest growing part is O(n^3) 
    a = random.randint(2,N)             # O(1) - 20 is not large enough to raise the time of randint
    for i in range(k):                  # O(k) - for loop loops k times
        if mod_exp(a, N - 1, N) != 1:   # O(n^3) - see mod_exp function
            return False                # O(1) - return is constant time 
    return True                         # O(1) - return is constant time 

def generate_large_prime(n_bits: int) -> int:   #O(n^4) since the function is performing an O(n^3) operation n times
    while(True):                                # O(n) - Testing random numbers for an average of n times is O(n)
        possible = random.getrandbits(n_bits)   # O(1) - retrieving a random number of bits is constant time 
        if fermat(possible,20):                 # O(n^3) - see fermat function
            return possible                     # O(1) - Returning is constant time 
```
O(n^4)

#### Space
TODO: SWITCH FROM TIME ANALYSIS TO SPACE
```
def mod_exp(x: int, y: int, N: int) -> int: # O(n^3) since there are n recursions with O(n^2) time
    if y == 0:                              # O(1) - comparison is constant time
        return 1;                           # O(1) - returning is constant time 
    z = mod_exp(x,y//2,N)                   # O(n) - each function call is O(n) time
    if y % 2 == 0:                          # O(1) - comparison is constant time 
        return (z ** 2) % N                 # O(n^2) - returning is constant time 
    else:                                   # O(1) - continuing to the alternate case is constant time 
        return (x * (z ** 2)) % N           # O(n^2) - calculation is constant time (because it uses the mod from earlier steps to keep number length shorter)

def fermat(N: int, k: int) -> bool:     # O(n^3) since the fastest growing part is O(n^3) 
    a = random.randint(2,N)             # O(1) - 20 is not large enough to raise the time of randint
    for i in range(k):                  # O(k) - for loop loops k times
        if mod_exp(a, N - 1, N) != 1:   # O(n^3) - see mod_exp function
            return False                # O(1) - return is constant time 
    return True                         # O(1) - return is constant time 

def generate_large_prime(n_bits: int) -> int:   #O(n^4) since the function is performing an O(n^3) operation n times
    while(True):                                # O(n) - Testing random numbers for an average of n times is O(n)
        possible = random.getrandbits(n_bits)   # O(1) - retrieving a random number of bits is constant time 
        if fermat(possible,20):                 # O(n^3) - see fermat function
            return possible                     # O(1) - Returning is constant time 
```
O(n^4)

### Empirical Data

| N    | time (sec)                  |
|------|-----------------------------|
| 64   | 0.0005166530609130859       |
| 128  | 0.0014758110046386719       |
| 256  | 0.027393817901611328        |
| 512  | 0.04432988166809082         |
| 1024 | max recursion depth reached |
| 2048 | max recursion depth reached |

### Comparison of Theoretical and Empirical Results

- Theoretical order of growth: O(n^4) 
- Empirical order of growth (if different from theoretical): O(n^3)

![empiricalPrimes.svg](empiricalPrimes.svg)

As the input grew, the amount of time it took to generate large primes stayed relatively stable compared to the theoretical likely because as n grew, it was more likely to get a working large prime on the first few tries.

## Core

### Design Experience
My discussion partners were Alyse Swenson and Emeline MacJanet.
We discussed the necessary functions, as well as the algorithm architecture. 
We also covered mypy helper functions that could provide redundancy.

### Theoretical Analysis - Key Pair Generation

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data

| N    | time (sec) |
|------|------------|
| 64   |            |
| 128  |            |
| 256  |            |
| 512  |            |
| 1024 |            |
| 2048 |            |

### Comparison of Theoretical and Empirical Results

- Theoretical order of growth: *copy from section above* 
- Empirical order of growth (if different from theoretical): 

![img](img.png)

*Fill me in*

## Stretch 1

### Design Experience
My discussion partners were Alyse Swenson and Emeline MacJanet.
We coordinated both the medium and people with whom we would be exchanging keys.
We briefly covered which encryption algorithm we would all be using. 

### Theoretical Analysis - Encrypt and Decrypt

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data

| N    | encryption time (sec) | decryption time (sec) |
|------|-----------------------|-----------------------|
| 64   |                       |                       |
| 128  |                       |                       |
| 256  |                       |                       |
| 512  |                       |                       |
| 1024 |                       |                       |
| 2048 |                       |                       |

### Comparison of Theoretical and Empirical Results

#### Encryption

- Theoretical order of growth: *copy from section above* 
- Empirical order of growth (if different from theoretical): 

![img](img.png)

*Fill me in*

#### Decryption

- Theoretical order of growth: *copy from section above* 
- Empirical order of growth (if different from theoretical): 

![img](img.png)

*Fill me in*

### Encrypting and Decrypting With A Classmate

*Fill me in*

## Stretch 2

### Design Experience
My discussion partners were Alyse Swenson and Emeline MacJanet.
We discussed implications of the Miller Rabin prime test.
We focused on the math and how it works.

### Probabilistic Natures of Fermat and Miller Rabin

### Results

*Fill me in*

### Discussion

*Fill me in*

## Project Review

*Fill me in*

