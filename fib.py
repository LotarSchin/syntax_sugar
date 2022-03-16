from functools import wraps


def profiler(func):
    calls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal calls
        if not calls:
            wrapper.calls = 0

        calls += 1
        result = func(*args, **kwargs)
        calls -= 1
        wrapper.calls += 1

        return result

    return wrapper


def timeit(f):
    def wrapper(*args):
        if args[0] == 35:  # check this number
            import time
            t0 = time.time()
            res = f(*args)
            t1 = time.time()
            print(f"Used time: {t1 - t0}")
        else:
            res = f(*args)
        return res

    return wrapper


def memorize(f):
    cache = {}

    def wrapper(*args):  # ez a sor volt rossz
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return wrapper  # es ez a sor volt rossz


# @profiler
@timeit
@memorize
def fib(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


# fib.calls = 0
a = fib(35)

print(a)
# print(fib.calls)


# 7 = (7) + (6 + 5) + (5+4) + (4 + 3)