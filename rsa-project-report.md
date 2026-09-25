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

#### Space
```
def mod_exp(x: int, y: int, N: int) -> int: # O(n) since there are n recursions taking up space
    if y == 0:                              # O(1) - comparison is constant space
        return 1;                           # O(1) - returning is constant space 
    z = mod_exp(x,y//2,N)                   # O(n) - recursion calls itself n times deep
    if y % 2 == 0:                          # O(1) - comparison is constant space 
        return (z ** 2) % N                 # O(1) - returning storage is constant 
    else:                                   # O(1) - continuing to the alternate case is constant space 
        return (x * (z ** 2)) % N           # O(1) - return storage is constant space

def fermat(N: int, k: int) -> bool:     # O(n) since the fastest growing part is O(n) 
    a = random.randint(2,N)             # O(1) - constant space N serves as a boundry making it linear storage
    for i in range(k):                  # O(1) - just stores the i in range (k), a constant
        if mod_exp(a, N - 1, N) != 1:   # O(n) - see mod_exp function
            return False                # O(1) - return is constant, just storing False 
    return True                         # O(1) - return is constant, just storing True 

def generate_large_prime(n_bits: int) -> int:   # O(n) since the function is storing an O(n) number of bits
    while(True):                                # O(1) - Testing random numbers for an average of n times is O(n)
        possible = random.getrandbits(n_bits)   # O(n) - retrieving an n number of bits takes n storage 
        if fermat(possible,20):                 # O(n) - see fermat function
            return possible                     # O(1) - Returning doesn't store anything new
```

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

```
def greatest_common_divisor(a: int, b: int):    # O(n^3) - since the recursion increases the time the most
    if b == 0:                                  # O(1) - comparison is constant time
        return a                                # O(1) - returning is constant time
    return greatest_common_divisor(b, a % b)    # O(n^3) - takes the mod and runs again

def extended_euclid(a: int, b: int) -> tuple[int, int, int]:    # O(n^3) - the fastest growing time use was O(n^2)
    if b == 0:                                                  # O(1) - comparison is constant time                
        return 1, 0, a                                          # O(1) - comparison is constant time
    [x,y,d] = extended_euclid(b, a % b)                         # O(n^3) - takes the mod and runs again, but the amount of recursion that will happen is linear
    return y, x - (a // b) * y, d                               # O(1) - only one new number calculated and the some values are returned

def generate_key_pairs(n_bits) -> tuple[int, int, int]:         # O(n^4) - O(n^4) was the fastest growing rate of space used
    p = prime_number_generation.generate_large_prime(n_bits)    # O(n^4) - see baseline section
    q = prime_number_generation.generate_large_prime(n_bits)    # O(n^4) - see baseline section
    N = p * q                                                   # O(n) - multiplying is linear time
    e = 2                                                       # O(1) - storing one more number is constant time
    m = (p-1) * (q-1)                                           # O(n) - multiplying is linear time
    while greatest_common_divisor(e, m) > 1:                    # O(n^3) - see greatest_common_divisor
        index = random.randint(0, 24)                           # O(1) - generating a fixed number betwewen 0 and 24 is constant time
        e = primes[index]                                       # O(1) - assigning a new variable is constant time
    d, y, g = extended_euclid(e, m)                             # O(n^3) - see extended_euclid reasoning
    if d < 0:                                                   # O(1) - comparison is constant time
        d = m + d                                               # O(1) - addition is constant time
    return N, e, d                                              # O(1) - returning is constant time
```

#### Space

```
def greatest_common_divisor(a: int, b: int):    # O(n) - the only new thing being stored is the new paremeters each function call if the variable b != 0
    if b == 0:                                  
        return a                                
    return greatest_common_divisor(b, a % b)    # O(n) - stores a linear amount of recursion frames

def extended_euclid(a: int, b: int) -> tuple[int, int, int]:                    # O(n) - the fastest growing storage use was O(n)
    if b == 0:                                                                  
        return 1, 0, a                                                          
    [x,y,d] = extended_euclid(b, a % b)                                         # O(n) - stores a linear amount of recursion frames and their return values
    return y, x - (a // b) * y, d                                               # O(1) - only one new number calculated and stored

def generate_key_pairs(n_bits) -> tuple[int, int, int]:         # O(n) - O(n) was the fastest growing rate of space used
    p = prime_number_generation.generate_large_prime(n_bits)    # O(n) - see baseline section
    q = prime_number_generation.generate_large_prime(n_bits)    # O(n) - see baseline section
    N = p * q                                                   # O(1) - storing one more number
    e = 2                                                       # O(1) - storing one more number
    m = (p-1) * (q-1)                                           # O(1) - storing one more number
    while greatest_common_divisor(e, m) > 1:                    
        index = random.randint(0, 24)                           # O(1) - 0 and 24 serve as barriers making it constant storage use
        e = primes[index]                                       # O(1) - one new variable
    d, y, g = extended_euclid(e, m)                             # O(n) - see extended_euclid reasoning
    if d < 0:                                                   
        d = m + d                                               # O(1) - 1 new value stored
    return N, e, d                                              
```

### Empirical Data

| N    | time (sec)            |
|------|-----------------------|
| 64   | 0.0014395713806152344 |
| 128  | 0.0064160823822021484 |
| 256  | 0.10974335670471191   |
| 512  | 0.6169900894165039    |
| 1024 | 2.578016519546509     |
| 2048 | 131.9463393688202     |

### Comparison of Theoretical and Empirical Results

- Theoretical order of growth: n^4 
- Empirical order of growth (if different from theoretical): n^3

![empiricalKeys.svg](empiricalKeys.svg)

The prime number generator, as observed earlier, is generally a bit faster than I theorized. That error influenced the theoretical speed of generating key pairs as getting primes is a part of making a key pair.

## Stretch 1

### Design Experience
My discussion partners were Alyse Swenson and Emeline MacJanet.
We coordinated both the medium and people with whom we would be exchanging keys.
We briefly covered which encryption algorithm we would all be using. 

### Theoretical Analysis - Encrypt and Decrypt

#### Time 
```
def transform(          # O(n^3) - the fastest growing part was O(n^3)
        data: bytes,            
        N: int,                 
        exponent: int,          
        in_chunk_bytes: int,    
        out_chunk_bytes: int,   
) -> bytes:
    out = []                                                    # O(1) - constant time to create an array
    for block in chunks(data, in_chunk_bytes):                  # O(n) - linear time in proportion to the amount of blocks
        if len(block) != in_chunk_bytes:                        # O(1) - comparison is constant time
            raise ValueError("Input not aligned to chunk size.")# O(1) - sending error message is constant time
        x = int.from_bytes(block, "big")                        # O(n) - iterable is linear time
        y = mod_exp(x, exponent, N)                             # O(n^3) - mod_exp is O(n^3) see baseline
        out.append(y.to_bytes(out_chunk_bytes, "big"))          # O(n) - appending time is in proportion to the number of bytes in the array
    return b"".join(out)                                        # O(n) - joining is linear time
```

#### Space

```
def transform(
        data: bytes,            
        N: int,                 
        exponent: int,          
        in_chunk_bytes: int,    
        out_chunk_bytes: int,   
) -> bytes:
    out = []                                                    # O(1) - establishing an array is linear space
    for block in chunks(data, in_chunk_bytes):                  # O(1) - making a for loop counter is linear space
        if len(block) != in_chunk_bytes:                        # O(1) - storing and comparing two groups of data is constant space
            raise ValueError("Input not aligned to chunk size.")# O(1) - storing the error to send is constant space
        x = int.from_bytes(block, "big")                        # O(n) - storing an n by m value, which is linear space
        y = mod_exp(x, exponent, N)                             # O(n) - see baseline mod_exp function
        out.append(y.to_bytes(out_chunk_bytes, "big"))          # O(n) - to append takes n by m space, which is linear
    return b"".join(out)                                        # O(n) - 
```

### Empirical Data

| N    | encryption time (sec) | decryption time (sec) |
|------|-----------------------|-----------------------|
| 64   | 0.02246880531311035   | 0.485                 |
| 128  | 0.015599727630615234  | 0.981                 |
| 256  | 0.01780390739440918   | 2.698                 |
| 512  | 0.03537154197692871   | 5.354                 |
| 1024 | 0.04913663864135742   | 19.634                |
| 2048 | 0.08700251579284668   |                       |

### Comparison of Theoretical and Empirical Results

#### Encryption

- Theoretical order of growth: O(n^3) 
- Empirical order of growth (if different from theoretical): O(n^(1/3))

![encrypt.svg](encrypt.svg)

I think that the blocks helped cut the time more in practice.

#### Decryption

- Theoretical order of growth: O(n^3) 
- Empirical order of growth (if different from theoretical): O(n^(1/3))

![decrypt.svg](decrypt.svg)

I think that the blocks helped cut the time more in practice.

### Encrypting and Decrypting With A Classmate

I encrypted and decrypted a file with Emeline MacJanet. It was successful, after I realized that the file could not be copy and pasted and had to be sent as is, and that I had also been mixing up the public and private keys.

## Stretch 2

### Design Experience

My discussion partners were Alyse Swenson and Emeline MacJanet.
We discussed implications of the Miller Rabin prime test.
We focused on the math and how it works.

### Probabilistic Natures of Fermat and Miller Rabin

### Results

Miller Rabin was able to correctly identify the carmicael numbers more consistently before the fermat could.
When I tested it with the carmichael number 561, it was able to consistently find it correctly false at k = 10, while the 
Fermat test could not.

### Discussion

The Miller Rabin algorithm is theoretically 25% more accurate than the Fermat algorithm.
This is reflected in my results when I tested the top 5 carmicael numbers with both.

## Project Review

My discussion partners were Alyse Swenson and Emeline MacJanet.
We discussed the various implimentations that we used, especially for the fermat function.
We also talked about how each of us went about finding the space complexity for various functions.

