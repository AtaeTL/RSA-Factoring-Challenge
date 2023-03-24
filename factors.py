import sys

def factorize(n):
    """Return a tuple of factors of n"""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return (i, n // i)
    return None

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

with open(sys.argv[1]) as f:
    for line in f:
        n = int(line)
        factors = factorize(n)
        if factors is not None:
            print(f"{n}={factors[0]}*{factors[1]}")
