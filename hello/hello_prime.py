import time

def forever():
    yield 999
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a+b

def is_prime(x):
    # only positive numbers are allowed and the smallest prime number is 2
    if (x > 1):
        divisor = 2
        # because the submit number can always be divided by itself we can use the
        # range function to set the correct range
        for i in range(divisor,x):
            if (x % i) == 0:
                return False
    else:
        return False
    return True

t = time.clock()
for y in (p for p in forever() if is_prime(p)):
    print("prime: {}".format(y))
    t1 = time.clock()
    print("eslaped: {}".format(t1-t))
    t = t1