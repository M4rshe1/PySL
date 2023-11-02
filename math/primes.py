from time import perf_counter
IN = 1000


def primes(n):
    """Return a list of prime numbers from 2 to n."""
    prime = []
    start = perf_counter()
    for i in range(2, n + 1):
        for p in prime:
            if i % p == 0:
                break
        else:
            prime.append(i)
    end = perf_counter()
    return prime, end - start


pr, t = primes(IN)

print("primes: ", len(pr), "in", IN)
print("time: ", t)
print(pr)
