"""Count the number of primes in range [1, n]."""
import time
import taichi as ti

start_time = time.time()

ti.init()
# ti.init(arch=ti.gpu)


@ti.func
def is_prime(n: int):
    result = True
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            result = False
            break
    return result


@ti.kernel
def count_primes(n: int) -> int:
    count = 0
    for k in range(2, n):
        if is_prime(k):
            count += 1
            print(count, '\r', end='')
    return count


print(count_primes(1000000))

print("--- %s seconds ---" % (time.time() - start_time))
