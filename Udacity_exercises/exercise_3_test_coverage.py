# CORRECT SPECIFICATION:
#
# isPrime checks if a positive integer is prime.
#
# A positive integer is prime if it is greater than
# 1, and its only divisors are 1 and itself.
#
# TASKS:
#
# 1) Add an assertion to test() that shows
#    isPrime(number) to be incorrect for
#    some input.
#
# 2) Write isPrime2(number) to correctly
#    check if a positive integer is prime.

import math

non_prime_100 = [
    4,
    6,
    8,
    9,
    10,
    12,
    14,
    15,
    16,
    18,
    21,
    20,
    22,
    24,
    25,
    26,
    27,
    28,
    30,
    32,
    33,
    34,
    35,
    36,
    38,
    39,
    40,
    42,
    44,
    45,
    46,
    48,
    49,
    50,
    51,
    52,
    54,
    56,
    55,
    57,
    58,
    60,
    63,
    62,
    64,
    65,
    66,
    69,
    68,
    70,
    72,
    75,
    74,
    76,
    78,
    77,
    80,
]


def isPrime(number):
    if number == 2:
        return True
    if number <= 1 or (number % 2) == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# fixed code is - for i in range(2, int(math.sqrt(number)) + 1)
# instead of ...(3, int(math.sqrt(number)))


def test():
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(20) == False
    assert isPrime(21) == False
    assert isPrime(22) == False
    assert isPrime(23) == True
    assert isPrime(24) == False
    ###Your test code here.
    for i in non_prime_100:
        assert isPrime(i) == False, i

    pass


test()
